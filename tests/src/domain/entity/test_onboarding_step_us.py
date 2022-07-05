from unittest.mock import MagicMock

import pytest

from func.src.domain.entity.onboarding_step_us import OnboardingUS

dummy_unique_id = "15619584"
dummy_complete_user = {
    "portfolios": {"default": {"us": {"dw_account": dummy_unique_id, "dw_id": dummy_unique_id}}},
    "unique_id": dummy_unique_id,
    "terms": {
        "term_open_account_dw": True,
        "term_application_dw": True,
        "term_and_privacy_policy_data_sharing_policy_dw": True,
        "term_disclosures_and_disclaimers": True,
        "term_money_corp": True,
        "term_gringo_world": True,
        "term_gringo_world_general_advices": True,
    },
    "external_exchange_requirements": {"us": {
        "is_politically_exposed": False,
        "is_exchange_member": False,
        "is_company_director": False,
        "external_fiscal_tax_confirmation": True,
        "user_employ_status": True,
        "time_experience": True,
        "w8_confirmation": True,
    }},
}
dummy_missing_steps_user = {
    "portfolios": {"default": {"us": {"dw_account": None, "dw_id": None}}},
    "unique_id": dummy_unique_id,
    # "terms": {
    #     "term_open_account_dw": None,
    #     "term_application_dw": None,
    #     "term_and_privacy_policy_data_sharing_policy_dw": None,
    #     "term_disclosures_and_disclaimers": None,
    #     "term_money_corp": None,
    #     "term_gringo_world": None,
    #     "term_gringo_world_general_advices": None,
    # },
    # "external_exchange_requirements": {"us": {
    #     "is_politically_exposed": None,
    #     "is_exchange_member": None,
    #     "is_company_director": None,
    #     "external_fiscal_tax_confirmation": None,
    #     "user_employ_status": None,
    #     "time_experience": None,
    #     "w8_confirmation": None,
    # }},
}


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_terms_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.terms_step(current_user)
    assert response == stopped_in_this_step


fake_check_if_exists_callback = MagicMock()


def test_user_document_validator_step_us():
    fake_check_if_exists_callback.return_value = False
    response = OnboardingUS.user_document_validator_step_us(fake_check_if_exists_callback)
    fake_check_if_exists_callback.assert_called_once_with()
    assert response is True


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_is_politically_exposed_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.is_politically_exposed_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_is_exchange_member_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.is_exchange_member_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_is_company_director_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.is_company_director_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_external_fiscal_tax_confirmation_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.external_fiscal_tax_confirmation_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_employ_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.employ_step(current_user)
    assert response == stopped_in_this_step


@pytest.mark.parametrize("user,stopped_in_step", [
    ({"portfolios": {"default": {}}, "external_exchange_requirements": {"us": {"time_experience": True}}}, True),
    ({"portfolios": {"default": {"us": {"dw_id": dummy_unique_id}}}}, True),
    (dummy_missing_steps_user, True),
    (dummy_complete_user, False),
])
def test_time_experience_step(user: dict, stopped_in_step: bool):
    response = OnboardingUS.time_experience_step(user)
    assert response == stopped_in_step


@pytest.mark.parametrize("current_user,stopped_in_this_step", [
    (dummy_complete_user, False),
    (dummy_missing_steps_user, True)
])
def test_w8_confirmation_step(current_user: dict, stopped_in_this_step: bool):
    response = OnboardingUS.w8_confirmation_step(current_user)
    assert response == stopped_in_this_step
