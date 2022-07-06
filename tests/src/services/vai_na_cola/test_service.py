from typing import Dict, List
from unittest.mock import patch, MagicMock, call

from func.src.domain.validator import Wallet, VaiNaColaWalletReport
from func.src.services.vai_na_cola.service import VaiNaColaService

dummy_id = "id1"
dummy_report = VaiNaColaWalletReport(
    id=dummy_id,
    influencer="Pendente de Definição",
    influencer_type="Pendente de Definição",
    report_date="Pendente de Definição",
    profitability="15%",
    rebalance_date="05/06/2022",
)
dummy_portfolio_report = [dummy_report, dummy_report]
dummy_wallet = MagicMock()
dummy_wallets_vnc_br = {dummy_id: dummy_wallet, "id2": dummy_wallet}
stub_portfolio = MagicMock(
    wallets_vnc_br=dummy_wallets_vnc_br
)


@patch.object(VaiNaColaService, "_request_vnc_br_portfolio_report", return_value=dummy_portfolio_report)
def test_get_vai_na_cola_portfolio_report(mocked_request_portfolio_report):
    response = VaiNaColaService.get_vai_na_cola_portfolio_report(stub_portfolio)
    mocked_request_portfolio_report.assert_called_once_with(dummy_wallets_vnc_br)
    assert response == dummy_portfolio_report


@patch.object(VaiNaColaService, "_request_vnc_br_portfolio_report", return_value=[])
def test_get_vai_na_cola_portfolio_report_empty(mocked_request_portfolio_report):
    response = VaiNaColaService.get_vai_na_cola_portfolio_report(stub_portfolio)
    mocked_request_portfolio_report.assert_called_once_with(dummy_wallets_vnc_br)
    assert response == []


@patch.object(VaiNaColaService, "_request_vnc_br_wallet_report", return_value=dummy_report)
def test_request_vnc_br_portfolio_report(mocked_request_wallet_report):
    response = VaiNaColaService._request_vnc_br_portfolio_report(dummy_wallets_vnc_br)
    mocked_request_wallet_report.assert_has_calls((call("id1", dummy_wallet), call("id2", dummy_wallet)))
    assert response == dummy_portfolio_report


@patch.object(VaiNaColaService, "_request_vnc_br_wallet_report")
def test_request_vnc_br_portfolio_report_empty(mocked_request_wallet_report):
    response = VaiNaColaService._request_vnc_br_portfolio_report({})
    mocked_request_wallet_report.assert_not_called()
    assert response == []


def test_request_vnc_br_wallet_report():
    response = VaiNaColaService._request_vnc_br_wallet_report(dummy_id, dummy_wallet)
    assert response == dummy_report
