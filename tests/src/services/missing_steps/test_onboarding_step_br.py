from unittest.mock import patch

import pytest
from decouple import AutoConfig

from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.enums import UserFileType
from func.src.repository.file.repository import FileRepository
from func.src.services.missing_steps.service_br import GetMissingStepBR

dummy_unique_id = "15619584"
dummy_complete_user = {
    "portfolios": {"default": {"br": {"bovespa_account": dummy_unique_id}}},
    "unique_id": dummy_unique_id
}


@pytest.fixture
def fake_onboarding_step_getter():
    return GetMissingStepBR(dummy_complete_user)


@pytest.fixture
def fake_onboarding_step_getter_with_empty_user():
    return GetMissingStepBR({})


@patch.object(OnboardingBR, "user_suitability_step")
@patch.object(OnboardingBR, "user_identifier_step")
@patch.object(OnboardingBR, "user_selfie_step")
@patch.object(OnboardingBR, "user_complementary_step")
@patch.object(OnboardingBR, "user_document_validator_step_br")
@patch.object(OnboardingBR, "user_data_validation_step")
@patch.object(OnboardingBR, "user_electronic_signature_step")
def test_get_steps(
    user_electronic_signature_step,
    user_data_validation_step,
    user_document_validator_step_br,
    user_complementary_step,
    user_selfie_step,
    user_identifier_step,
    user_suitability_step,
    fake_onboarding_step_getter
):
    steps = fake_onboarding_step_getter._get_steps()
    for step in steps.values():
        step()
    user_electronic_signature_step.assert_called_once_with(dummy_complete_user)
    user_data_validation_step.assert_called_once_with(dummy_complete_user)
    user_document_validator_step_br.assert_called_once_with(dummy_complete_user,
                                                            fake_onboarding_step_getter._check_document_validator_step_br)
    user_complementary_step.assert_called_once_with(dummy_complete_user)
    user_selfie_step.assert_called_once_with(fake_onboarding_step_getter._check_if_selfie_exists)
    user_identifier_step.assert_called_once_with(dummy_complete_user)
    user_suitability_step.assert_called_once_with(dummy_complete_user)


def test_nothing_is_missing_true(fake_onboarding_step_getter):
    response = fake_onboarding_step_getter._nothing_is_missing()
    assert response is True


def test_nothing_is_missing_false(fake_onboarding_step_getter_with_empty_user):
    response = fake_onboarding_step_getter_with_empty_user._nothing_is_missing()
    assert response is False


@patch.object(AutoConfig, "__call__", return_value=True)
@patch.object(FileRepository, "user_file_exists", return_value=True)
def test_check_if_selfie_exists(mocked_file_repository, mocked_env, fake_onboarding_step_getter):
    response = fake_onboarding_step_getter._check_if_selfie_exists()
    mocked_file_repository.assert_called_once_with(
        file_type=UserFileType.SELFIE,
        unique_id=dummy_unique_id,
        bucket_name=True,
    )
    assert response is True


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
def test_check_document_validator_step_br(
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
    response = fake_onboarding_step_getter._check_document_validator_step_br()
    assert response == expected
