from unittest.mock import MagicMock

from func.src.domain.models.snapshots.vai_na_cola import VaiNaColaReport

dummy_empty_user = []
expected_snapshot_empty = []


def test_model_instance_empty():
    snapshot = VaiNaColaReport(dummy_empty_user).get_snapshot()
    assert snapshot == expected_snapshot_empty


dummy_wallet = [MagicMock(id=None)]*3
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


def test_model_instance():
    snapshot = VaiNaColaReport(dummy_wallet).get_snapshot()
    assert snapshot == expected_snapshot
