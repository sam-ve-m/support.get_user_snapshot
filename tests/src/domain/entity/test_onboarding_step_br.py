from unittest.mock import patch, MagicMock

import pytest
from decouple import AutoConfig

from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.enums import UserFileType, CAFStatus
from func.src.repository.file.repository import FileRepository

dummy_unique_id = "15619584"
dummy_complete_user = {
    "portfolios": {"default": {"br": {"bovespa_account": dummy_unique_id}}},
    "unique_id": dummy_unique_id,
    "suitability": {"suit": "ability"},
    "terms": {"term_refusal": False},
    "identifier_document": {"cpf": True},
    "phone": True,
    "marital": True,
    "bureau_status": CAFStatus.APPROVED.value,
    "is_bureau_data_validated": True,
    "electronic_signature": True,
}
dummy_missing_steps_user = {
    "portfolios": {"default": {"br": {"bovespa_account": None}}},
    "unique_id": dummy_unique_id,
    "suitability": None,
    # "terms": None,
    # "identifier_document": None,
    "phone": None,
    "marital": None,
    "bureau_status": CAFStatus.DOCUMENT.value,
    "is_bureau_data_validated": False,
    "electronic_signature": False
}


@pytest.mark.parametrize("user,stopped_in_step", [
    ({"suitability": {"suit": "ability"}}, False),
    ({"terms": {"term_refusal": False}}, False),
    (dummy_missing_steps_user, True),
    (dummy_complete_user, False),
])
def test_user_suitability_step(user: dict, stopped_in_step: bool):
    response = OnboardingBR.user_suitability_step(user)
    assert response is stopped_in_step


@pytest.mark.parametrize("user,stopped_in_step", [
    ({"identifier_document": {"cpf": True}}, False),
    (dummy_missing_steps_user, True),
    (dummy_complete_user, False),
    ({"phone": True}, False),
])
def test_user_identifier_step(user: dict, stopped_in_step: bool):
    response = OnboardingBR.user_identifier_step(user)
    assert response is stopped_in_step


fake_check_if_exists_callback = MagicMock()


def test_user_selfie_step():
    fake_check_if_exists_callback.return_value = True
    response = OnboardingBR.user_selfie_step(fake_check_if_exists_callback)
    fake_check_if_exists_callback.assert_called_with()
    assert response is False


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_user_complementary_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingBR.user_complementary_step(current_user)
    assert response == stopped_in_this_step


def test_user_document_validator_step_br_not_in_document_bureau_status():
    response = OnboardingBR.user_document_validator_step_br(dummy_missing_steps_user, fake_check_if_exists_callback)
    fake_check_if_exists_callback.assert_called_with()
    assert response is False


def test_user_document_validator_step_br():
    fake_check_if_exists_callback.return_value = False
    response = OnboardingBR.user_document_validator_step_br(dummy_missing_steps_user, fake_check_if_exists_callback)
    fake_check_if_exists_callback(dummy_missing_steps_user)
    assert response is True


def test_user_document_validator_step_br_bureau_validated():
    response = OnboardingBR.user_document_validator_step_br(dummy_complete_user, fake_check_if_exists_callback)
    assert response is None


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_user_data_validation_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingBR.user_data_validation_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_user_electronic_signature_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingBR.user_electronic_signature_step(current_user)
    assert response == stopped_in_this_step
