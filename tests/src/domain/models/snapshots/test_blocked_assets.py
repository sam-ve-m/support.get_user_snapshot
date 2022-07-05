from unittest.mock import MagicMock

from func.src.domain.models.snapshots.blocked_assets import BlockedAssets
import pytest


dummy_blocked_assets = [MagicMock(
    ticker="Pendente de Definição",
    mean_price="Pendente de Definição",
    current_quantity="Pendente de Definição",
)]*3


@pytest.fixture()
def fake_blocked_assets_model():
    return BlockedAssets(dummy_blocked_assets)


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
