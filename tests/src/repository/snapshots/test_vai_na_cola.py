from func.src.repository.snapshots.vai_na_cola import VaiNaColaSnapshotRepository
from unittest.mock import patch


dummy_bovespa_account = "159951"
dummy_complete_user = {'portfolios': {'vnc': {'br': [{"bovespa_account": dummy_bovespa_account}]*3}}}
dummy_empty_user = {}


@patch.object(VaiNaColaSnapshotRepository, "_request_vnc_wallet_data")
def test_snapshot(mocked_request_wallet):
    mocked_request_wallet.return_value = None
    response = VaiNaColaSnapshotRepository.snapshot(dummy_complete_user)
    mocked_request_wallet.assert_called_with(dummy_bovespa_account)
    assert response == [None]*3


@patch.object(VaiNaColaSnapshotRepository, "_request_vnc_wallet_data")
def test_snapshot_no_accounts(mocked_request_wallet):
    response = VaiNaColaSnapshotRepository.snapshot(dummy_empty_user)
    mocked_request_wallet.assert_not_called()
    assert response == []


expected_fields = (
    "Carteira/Código",
    "Influencer",
    "Tipo Influencer",
    "Data de referência",
    "Rentabilidade Vai na Cola",
    "Desenquadrado"
)


def test_request_vnc_wallet_data():
    response = VaiNaColaSnapshotRepository._request_vnc_wallet_data(dummy_bovespa_account)
    assert all((field in response.keys() for field in expected_fields))