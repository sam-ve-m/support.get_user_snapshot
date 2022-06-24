from func.src.domain.models.snapshots.blocked_assets import BlockedAssets
from unittest.mock import patch
import pytest

dummy_user = {}
dummy_blocked_assets = [{}, {}, {}]


@pytest.fixture()
def fake_blocked_assets_model():
    with patch.object(BlockedAssets, "_request_blocked_assets", return_value=dummy_blocked_assets):
        return BlockedAssets(dummy_user)


@patch.object(BlockedAssets, "_request_blocked_assets")
def test_model_instance(mocked_request):
    BlockedAssets(dummy_user)
    mocked_request.assert_called_once_with(dummy_user)


def test_request_blocked_assets(fake_blocked_assets_model):
    blocked_assets = fake_blocked_assets_model._request_blocked_assets(dummy_user)
    assert dummy_blocked_assets == blocked_assets


expected_snapshot = [[
    {'value': 'Pendente de Definição', 'label': 'Ativo'},
    {'value': 'Pendente de Definição', 'label': 'Preço Médio'},
    {'value': 'Pendente de Definição', 'label': 'Quantidade'}
], [
    {'value': 'Pendente de Definição', 'label': 'Ativo'},
    {'value': 'Pendente de Definição', 'label': 'Preço Médio'},
    {'value': 'Pendente de Definição', 'label': 'Quantidade'}
], [
    {'value': 'Pendente de Definição', 'label': 'Ativo'},
    {'value': 'Pendente de Definição', 'label': 'Preço Médio'},
    {'value': 'Pendente de Definição', 'label': 'Quantidade'}
]]


def test_get_snapshot(fake_blocked_assets_model):
    snapshot = fake_blocked_assets_model.get_snapshot()
    assert expected_snapshot == snapshot
