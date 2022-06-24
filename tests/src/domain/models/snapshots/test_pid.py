import pytest

from func.src.domain.models.snapshots.pid import PID

dummy_complete_user_data = {
    "email": True,
    "cel_phone": True,
    "identifier_document": {"cpf": True, "document_data": {"number": True}},
    "birth_date": True,
    "portfolios": {"vnc": {"br": True}},
    "mother_name": True,
    "address": {"zip_code": True},
}

dummy_missing_user_data = {
    "email": None,
    "cel_phone": None,
    # "identifier_document": {"cpf": None, "document_data": {"number": None}},
    "birth_date": None,
    # "portfolios": {"vnc": {"br": None}},
    "mother_name": None,
    # "address": {"zip_code": None},
}


def test_set_email_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "email": dummy_missing_user_data.get("email")
    }
    with pytest.raises(Exception):
        PID(dummy_user_data).get_snapshot()


def test_set_telefone_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "cel_phone": dummy_missing_user_data.get("cel_phone")
    }
    expected_field = {"label": "Telefone", "value": PID.NOT_FOUND_MESSAGE}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot


def test_set_cpf_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
    }
    identifier_document = dummy_user_data.get("identifier_document")
    dummy_user_data.update({"identifier_document": {**identifier_document, "cpf": dummy_missing_user_data.get("cpf")}})
    with pytest.raises(Exception):
        PID(dummy_user_data).get_snapshot()


def test_set_data_nascimento_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "birth_date": dummy_missing_user_data.get("birth_date")
    }
    expected_field = {"label": "Data Nascimento", "value": PID.NOT_FOUND_MESSAGE}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot


def test_set_possui_vai_na_cola_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "portfolios": dummy_missing_user_data.get("portfolios", {})
    }
    expected_field = {"label": "Possui Vai na Cola?", "value": False}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot


def test_set_rg_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
    }
    identifier_document = dummy_user_data.get("identifier_document")
    dummy_user_data.update({"identifier_document": {**identifier_document, "document_data": dummy_missing_user_data.get("document_data", {})}})
    expected_field = {"label": "RG", "value": PID.NOT_FOUND_MESSAGE}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot


def test_set_nome_da_mae_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "mother_name": dummy_missing_user_data.get("mother_name")
    }
    expected_field = {"label": "Nome da Mãe", "value": PID.NOT_FOUND_MESSAGE}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot


def test_set_cep_not_in_snapshot():
    dummy_user_data = {
        **dummy_complete_user_data,
        "address": dummy_missing_user_data.get("address", {})
    }
    expected_field = {"label": "CEP", "value": PID.NOT_FOUND_MESSAGE}
    snapshot = PID(dummy_user_data).get_snapshot()
    assert expected_field in snapshot
