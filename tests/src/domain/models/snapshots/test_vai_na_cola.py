from func.src.domain.models.snapshots.vai_na_cola import VaiNaCola
from unittest.mock import patch, call
import pytest


dummy_bovespa_account = "159951"
dummy_complete_user = {'portfolios': {'vnc': {'br': [{"bovespa_account": dummy_bovespa_account}]*3}}}
dummy_empty_user = {}
dummy_wallet = {}


@pytest.fixture()
def fake_vai_na_cola_model():
    with patch.object(VaiNaCola, "_request_vnc_wallet_data", return_value=dummy_wallet):
        return VaiNaCola(dummy_complete_user)


expected_snapshot_empty = []


@patch.object(VaiNaCola, "_request_vnc_wallet_data", return_value=dummy_wallet)
def test_model_instance_empty(mocked_vai_na_cola_br):
    snapshot = VaiNaCola(dummy_empty_user).get_snapshot()
    mocked_vai_na_cola_br.assert_not_called()
    assert snapshot == expected_snapshot_empty


expected_snapshot = [[
        {'value': None, 'label': 'Carteira/Código'},
        {'value': 'Pendente de Definição', 'label': 'Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Tipo Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Data de referência'},
        {'value': '15%', 'label': 'Rentabilidade Vai na Cola'},
        {'value': '05/06/2022', 'label': 'Desenquadrado'}
    ], [
        {'value': None, 'label': 'Carteira/Código'},
        {'value': 'Pendente de Definição', 'label': 'Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Tipo Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Data de referência'},
        {'value': '15%', 'label': 'Rentabilidade Vai na Cola'},
        {'value': '05/06/2022', 'label': 'Desenquadrado'}
    ], [
        {'value': None, 'label': 'Carteira/Código'},
        {'value': 'Pendente de Definição', 'label': 'Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Tipo Influencer'},
        {'value': 'Pendente de Definição', 'label': 'Data de referência'},
        {'value': '15%', 'label': 'Rentabilidade Vai na Cola'},
        {'value': '05/06/2022', 'label': 'Desenquadrado'}
]]


@patch.object(VaiNaCola, "_request_vnc_wallet_data", return_value=dummy_wallet)
def test_model_instance(mocked_vai_na_cola_br):
    snapshot = VaiNaCola(dummy_complete_user).get_snapshot()
    mocked_vai_na_cola_br.assert_has_calls([call(dummy_bovespa_account)]*3)
    assert snapshot == expected_snapshot
