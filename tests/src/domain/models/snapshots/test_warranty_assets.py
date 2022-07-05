from unittest.mock import MagicMock

from func.src.domain.models.snapshots.warranty_assets import WarrantyAssets

dummy_user_data = {}
dummy_assets = [MagicMock(
    ticker="Pendente de Definição",
    current_value="Pendente de Definição",
    current_quantity="Pendente de Definição",
)]*2
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
    ]
]
expected_assets_empty = []


def test_snapshot_empty():
    snapshot = WarrantyAssets(dummy_assets_empty).get_snapshot()
    assert snapshot == expected_assets_empty


def test_snapshot():
    snapshot = WarrantyAssets(dummy_assets).get_snapshot()
    assert snapshot == expected_assets

