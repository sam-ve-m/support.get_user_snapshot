from unittest.mock import MagicMock

from func.src.domain.models.snapshots.wallet import BaseWallet

dummy_bovespa_id = "159951"
dummy_assets = [MagicMock(
    ticker='PETR4',
    mean_price=15.45,
    current_quantity=400,
    initial_quantity=150,
    spent_value=618,
    current_value=16,
)]*2

expected_snapshot = [[
    {'value': '159951', 'label': 'Código de bolsa'},
    {'value': 'Brazuca', 'label': 'Nome da carteira'},
    {'value': 'PETR4', 'label': 'Ativo'},
    {'value': 15.45, 'label': 'Preço Médio'},
    {'value': 400, 'label': 'Quantidade'},
    {'value': 150, 'label': 'Quantidade inicial'},
    {'value': 618, 'label': 'Valor Gasto'},
    {'value': 16, 'label': 'Valor Atual'}
]]*2
dummy_wallet_name = "Brazuca"


def test_snapshot(monkeypatch):
    setattr(BaseWallet, "wallet_name", dummy_wallet_name)
    snapshot = BaseWallet(dummy_bovespa_id, dummy_assets).get_snapshot()
    assert snapshot == expected_snapshot

