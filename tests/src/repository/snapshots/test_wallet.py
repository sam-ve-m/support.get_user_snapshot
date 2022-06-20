from typing import List

from func.src.repository.snapshots.wallet import WalletSnapshotRepository
from unittest.mock import patch, call


dummy_bovespa_id = "159951"
dummy_dw_account = "951159"
dummy_vnc_accounts = [{"bovespa_account": 1}, {"bovespa_account": 2}]
dummy_default_wallets = {"br": {"bovespa_account": dummy_bovespa_id}, "us": {"dw_account": dummy_dw_account}}
dummy_user_data = {"portfolios": {"default": dummy_default_wallets, "vnc": {"br": dummy_vnc_accounts}}}

dummy_default_wallets_ids = {"default_id": "Some Name"}
dummy_vnc_wallets_ids = {1: "Vai na Cola", 2: "Vai na Cola"}
dummy_single_portfolio_response = [True]
dummy_portfolios_responses = [True, True, True]


@patch.object(WalletSnapshotRepository, "_find_default_wallets_ids", return_value=dummy_default_wallets_ids)
@patch.object(WalletSnapshotRepository, "_find_vnc_wallets_ids", return_value=dummy_vnc_wallets_ids)
@patch.object(WalletSnapshotRepository, "_request_wallet_portfolio", return_value=dummy_single_portfolio_response)
def test_snapshot(mocked_request_portfolio, mocked_find_vnc_wallets, mocked_finds_defaults_wallets):
    response = WalletSnapshotRepository.snapshot(dummy_user_data)
    assert response == dummy_portfolios_responses
    mocked_finds_defaults_wallets.assert_called_once_with(dummy_user_data)
    mocked_find_vnc_wallets.assert_called_once_with(dummy_user_data)
    mocked_request_portfolio.assert_has_calls((call("Some Name", "default_id"), call("Vai na Cola", 1), call("Vai na Cola", 2)))


dummy_br_wallet_id = {"br_id": "Some Name"}
dummy_us_wallet_id = {"us_id": "Some Name"}
expected_defaults_ids = {"br_id": "Some Name", "us_id": "Some Name"}


@patch.object(WalletSnapshotRepository, "_find_wallet_id_br", return_value=dummy_br_wallet_id)
@patch.object(WalletSnapshotRepository, "_find_wallet_id_us", return_value=dummy_us_wallet_id)
def test_find_default_wallets_ids(mocked_find_wallet_id_us, mocked_find_wallet_id_br):
    response = WalletSnapshotRepository._find_default_wallets_ids(dummy_user_data)
    mocked_find_wallet_id_br.assert_called_once_with(dummy_default_wallets)
    mocked_find_wallet_id_us.assert_called_once_with(dummy_default_wallets)
    assert response == expected_defaults_ids


def test_find_wallet_id_br():
    response = WalletSnapshotRepository._find_wallet_id_br(dummy_default_wallets)
    assert response == {dummy_bovespa_id: "Brazuca"}


def test_find_wallet_id_us():
    response = WalletSnapshotRepository._find_wallet_id_us(dummy_default_wallets)
    assert response == {dummy_dw_account: "Gringa"}


dummy_missing_wallets = {}


def test_find_wallet_id_br_missing_wallets():
    response = WalletSnapshotRepository._find_wallet_id_br(dummy_missing_wallets)
    assert response == {}


def test_find_wallet_id_us_missing_wallets():
    response = WalletSnapshotRepository._find_wallet_id_us(dummy_missing_wallets)
    assert response == {}


def test_find_vnc_wallets_ids():
    response = WalletSnapshotRepository._find_vnc_wallets_ids(dummy_user_data)
    assert response == dummy_vnc_wallets_ids


expected_fields = (
    "Código de bolsa",
    "Nome da carteira",
    "Ativo",
    "Preço Médio",
    "Quantidade",
    "Quantidade inicial",
    "Valor Gasto",
    "Valor Atual",
)


def test_request_wallet_portfolio():
    response = WalletSnapshotRepository._request_wallet_portfolio("Brazuca", dummy_bovespa_id)
    for row in response:
        assert all((field in row.keys() for field in expected_fields))
