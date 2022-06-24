from unittest.mock import patch

from func.src.domain.models.snapshots.warranty_assets import WarrantyAssets

dummy_user_data = {}
dummy_assets = ["asset"]*2
dummy_assets_empty = []
expected_assets = [
    [
        {'value': 'Pendente de Definição', 'label': 'Ativo'},
        {'value': 'Pendente de Definição', 'label': 'Valor'},
        {'value': 'Pendente de Definição', 'label': 'Quantidade'}
    ], [
        {'value': 'Pendente de Definição', 'label': 'Ativo'},
        {'value': 'Pendente de Definição', 'label': 'Valor'},
        {'value': 'Pendente de Definição', 'label': 'Quantidade'}
]]
expected_assets_empty = []


@patch.object(WarrantyAssets, "_request_blocked_assets", return_value=dummy_assets_empty)
def test_snapshot_empty(mocked_request_warranty_assets):
    snapshot = WarrantyAssets(dummy_user_data).get_snapshot()
    mocked_request_warranty_assets.assert_called_once_with(dummy_user_data)
    assert snapshot == expected_assets_empty


@patch.object(WarrantyAssets, "_request_blocked_assets", return_value=dummy_assets)
def test_snapshot(mocked_request_warranty_assets):
    snapshot = WarrantyAssets(dummy_user_data).get_snapshot()
    mocked_request_warranty_assets.assert_called_once_with(dummy_user_data)
    assert snapshot == expected_assets

