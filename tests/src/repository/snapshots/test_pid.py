import pytest

from func.src.repository.snapshots.pid import PIDSnapshotRepository
from unittest.mock import patch


@patch.object(PIDSnapshotRepository, "_set_email_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_telefone_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_cpf_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_data_nascimento_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_possui_vai_na_cola_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_rg_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_nome_da_mae_in_snapshot")
@patch.object(PIDSnapshotRepository, "_set_cep_in_snapshot")
def test_snapshot(
        mocked_set_email_in_snapshot,
        mocked_set_telefone_in_snapshot,
        mocked_set_cpf_in_snapshot,
        mocked_set_data_nascimento_in_snapshot,
        mocked_set_possui_vai_na_cola_in_snapshot,
        mocked_set_rg_in_snapshot,
        mocked_set_nome_da_mae_in_snapshot,
        mocked_set_cep_in_snapshot,
):
    response = PIDSnapshotRepository.snapshot({})
    mocked_set_email_in_snapshot.assert_called_once()
    mocked_set_telefone_in_snapshot.assert_called_once()
    mocked_set_cpf_in_snapshot.assert_called_once()
    mocked_set_data_nascimento_in_snapshot.assert_called_once()
    mocked_set_possui_vai_na_cola_in_snapshot.assert_called_once()
    mocked_set_rg_in_snapshot.assert_called_once()
    mocked_set_nome_da_mae_in_snapshot.assert_called_once()
    mocked_set_cep_in_snapshot.assert_called_once()
    assert response == {}


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


def test_set_email_in_snapshot():
    spy_snapshot = {}
    dummy_label = "EMAIL"
    PIDSnapshotRepository._set_email_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)
    assert spy_snapshot == {dummy_label: True}


def test_set_email_in_snapshot_missing_email():
    with pytest.raises(Exception):
        PIDSnapshotRepository._set_email_in_snapshot({}, "", dummy_missing_user_data)


def test_set_telefone_in_snapshot():
    spy_snapshot = {}
    dummy_label = "TELEFONE"
    PIDSnapshotRepository._set_telefone_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_telefone_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "TELEFONE"
    PIDSnapshotRepository._set_telefone_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: PIDSnapshotRepository.NOT_FOUND_MESSAGE}


def test_set_cpf_in_snapshot():
    spy_snapshot = {}
    dummy_label = "CPF"
    PIDSnapshotRepository._set_cpf_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_cpf_in_snapshot_missing_cpf():
    with pytest.raises(Exception):
        PIDSnapshotRepository._set_cpf_in_snapshot({}, "", dummy_missing_user_data)


def test_set_data_nascimento_in_snapshot():
    spy_snapshot = {}
    dummy_label = "Data Nascimento"
    PIDSnapshotRepository._set_data_nascimento_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_data_nascimento_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "Data Nascimento"
    PIDSnapshotRepository._set_data_nascimento_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: PIDSnapshotRepository.NOT_FOUND_MESSAGE}


def test_set_possui_vai_na_cola_in_snapshot():
    spy_snapshot = {}
    dummy_label = "Possui Vai Na Cola"
    PIDSnapshotRepository._set_possui_vai_na_cola_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_possui_vai_na_cola_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "Possui Vai Na Cola"
    PIDSnapshotRepository._set_possui_vai_na_cola_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: False}


def test_set_rg_in_snapshot():
    spy_snapshot = {}
    dummy_label = "RG"
    PIDSnapshotRepository._set_rg_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_rg_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "RG"
    PIDSnapshotRepository._set_rg_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: PIDSnapshotRepository.NOT_FOUND_MESSAGE}


def test_set_nome_da_mae_in_snapshot():
    spy_snapshot = {}
    dummy_label = "Nome Da Mae"
    PIDSnapshotRepository._set_nome_da_mae_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_nome_da_mae_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "Nome Da Mae"
    PIDSnapshotRepository._set_nome_da_mae_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: PIDSnapshotRepository.NOT_FOUND_MESSAGE}


def test_set_cep_in_snapshot():
    spy_snapshot = {}
    dummy_label = "CEP"
    PIDSnapshotRepository._set_cep_in_snapshot(spy_snapshot, dummy_label, dummy_complete_user_data)


def test_set_cep_in_snapshot_missing_data():
    spy_snapshot = {}
    dummy_label = "CEP"
    PIDSnapshotRepository._set_cep_in_snapshot(spy_snapshot, dummy_label, dummy_missing_user_data)
    assert spy_snapshot == {dummy_label: PIDSnapshotRepository.NOT_FOUND_MESSAGE}
