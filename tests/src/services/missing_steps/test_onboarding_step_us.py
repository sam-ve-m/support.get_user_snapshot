from unittest.mock import patch

import pytest
from decouple import AutoConfig

from func.src.domain.entity.onboarding_step_us import OnboardingUS
from func.src.domain.enums import CAFStatus
from func.src.domain.enums import UserFileType
from func.src.repository.file.repository import FileRepository
from func.src.services.missing_steps.service_us import GetMissingStepUS


dummy_unique_id = "15619584"
dummy_complete_user = {
    "portfolios": {"default": {"us": {"dw_account": dummy_unique_id, "dw_id": dummy_unique_id}}},
}


@pytest.fixture
def fake_onboarding_step_getter():
    return GetMissingStepUS(dummy_complete_user)


@pytest.fixture
def fake_onboarding_step_getter_with_empty_user():
    return GetMissingStepUS({})


@patch.object(OnboardingUS, "terms_step")
@patch.object(OnboardingUS, "user_document_validator_step_us")
@patch.object(OnboardingUS, "is_politically_exposed_step")
@patch.object(OnboardingUS, "is_exchange_member_step")
@patch.object(OnboardingUS, "is_company_director_step")
@patch.object(OnboardingUS, "external_fiscal_tax_confirmation_step")
@patch.object(OnboardingUS, "employ_step")
@patch.object(OnboardingUS, "time_experience_step")
@patch.object(OnboardingUS, "w8_confirmation_step")
def test_get_steps(
    w8_confirmation_step,
    time_experience_step,
    employ_step,
    external_fiscal_tax_confirmation_step,
    is_company_director_step,
    is_exchange_member_step,
    is_politically_exposed_step,
    user_document_validator_step_us,
    terms_step,
    fake_onboarding_step_getter
):
    steps = fake_onboarding_step_getter._get_steps()
    for step in steps.values():
        step()
    w8_confirmation_step.assert_called_once_with(dummy_complete_user)
    time_experience_step.assert_called_once_with(dummy_complete_user)
    user_document_validator_step_us.assert_called_once_with(
        fake_onboarding_step_getter._check_document_validator_step_us)
    external_fiscal_tax_confirmation_step.assert_called_once_with(dummy_complete_user)
    is_company_director_step.assert_called_once_with(dummy_complete_user)
    is_exchange_member_step.assert_called_once_with(dummy_complete_user)
    is_politically_exposed_step.assert_called_once_with(dummy_complete_user)
    employ_step.assert_called_once_with(dummy_complete_user)
    terms_step.assert_called_once_with(dummy_complete_user)


def test_nothing_is_missing_true(fake_onboarding_step_getter):
    response = fake_onboarding_step_getter._nothing_is_missing()
    assert response is True


def test_nothing_is_missing_false(fake_onboarding_step_getter_with_empty_user):
    response = fake_onboarding_step_getter_with_empty_user._nothing_is_missing()
    assert response is False


missing_back_document = False, True, False
missing_front_document = True, False, False
missing_both_document = False, False, False
with_all_document = True, True, True


@pytest.mark.parametrize("doc_back_exists,doc_front_exists,expected", [
    missing_back_document,
    missing_front_document,
    missing_both_document,
    with_all_document,
])
@patch.object(AutoConfig, "__call__")
@patch.object(FileRepository, "user_file_exists")
def test_check_document_validator_step_us(
        mocked_file_repository,
        mocked_env,
        doc_back_exists: bool,
        doc_front_exists: bool,
        expected: bool,
        fake_onboarding_step_getter,
):
    docs_exists = {
        UserFileType.DOCUMENT_BACK: doc_back_exists,
        UserFileType.DOCUMENT_FRONT: doc_front_exists,
    }

    async def aux(file_type, **kwargs):
        return docs_exists.get(file_type)

    mocked_file_repository.side_effect = aux
    response = fake_onboarding_step_getter._check_document_validator_step_us()
    assert response == expected
