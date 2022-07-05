# import asyncio
# from unittest.mock import patch
#
# import pytest
# from decouple import config, AutoConfig
#
# from func.src.domain.entity.onboarding_step_us import OnboardingUS
# from func.src.domain.enums import UserFileType, TermsFileType
# from func.src.repository.file.repository import FileRepository
#
#
# dummy_unique_id = "15619584"
# dummy_complete_user = {
#     "portfolios": {"default": {"us": {"dw_account": dummy_unique_id, "dw_id": dummy_unique_id}}},
#     "unique_id": dummy_unique_id,
#     "terms": {
#         "term_open_account_dw": True,
#         "term_application_dw": True,
#         "term_and_privacy_policy_data_sharing_policy_dw": True,
#         "term_disclosures_and_disclaimers": True,
#         "term_money_corp": True,
#         "term_gringo_world": True,
#         "term_gringo_world_general_advices": True,
#     },
#     "external_exchange_requirements": {"us": {
#         "is_politically_exposed": False,
#         "is_exchange_member": False,
#         "is_company_director": False,
#         "external_fiscal_tax_confirmation": True,
#         "user_employ_status": True,
#         "time_experience": True,
#         "w8_confirmation": True,
#     }},
# }
# dummy_missing_steps_user = {
#     "portfolios": {"default": {"us": {"dw_account": None, "dw_id": None}}},
#     "unique_id": dummy_unique_id,
#     # "terms": {
#     #     "term_open_account_dw": None,
#     #     "term_application_dw": None,
#     #     "term_and_privacy_policy_data_sharing_policy_dw": None,
#     #     "term_disclosures_and_disclaimers": None,
#     #     "term_money_corp": None,
#     #     "term_gringo_world": None,
#     #     "term_gringo_world_general_advices": None,
#     # },
#     # "external_exchange_requirements": {"us": {
#     #     "is_politically_exposed": None,
#     #     "is_exchange_member": None,
#     #     "is_company_director": None,
#     #     "external_fiscal_tax_confirmation": None,
#     #     "user_employ_status": None,
#     #     "time_experience": None,
#     #     "w8_confirmation": None,
#     # }},
# }
#
#
# def test_find_missing_step_has_dw_account():
#     response = OnboardingUS.find_missing_step(dummy_complete_user)
#     assert response == "Nada"
#
#
# fake_func = "_fake_function"
# dummy_missing_step_label = "Label"
# fake_missing_steps_us = {
#     fake_func: dummy_missing_step_label
# }
#
#
# def test_find_missing_step_has_missing_step(monkeypatch):
#     monkeypatch.setattr(OnboardingUS, "_steps_us", fake_missing_steps_us)
#     setattr(OnboardingUS, fake_func, lambda x: True)
#     response = OnboardingUS.find_missing_step(dummy_missing_steps_user)
#     assert response == dummy_missing_step_label
#
#
# fake_complete_steps_us = {
#     fake_func: dummy_missing_step_label
# }
#
#
# def test_find_missing_step_no_missing_step(monkeypatch):
#     monkeypatch.setattr(OnboardingUS, "_steps_us", fake_complete_steps_us)
#     setattr(OnboardingUS, fake_func, lambda x: False)
#     response = OnboardingUS.find_missing_step(dummy_missing_steps_user)
#     assert response == "Nada"
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_terms_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._terms_step(current_user)
#     assert response == stopped_in_this_step
#
#
# missing_back_document = False, True, False
# missing_front_document = True, False, False
# missing_both_document = False, False, False
# with_all_document = True, True, True
#
#
# @pytest.mark.parametrize("doc_back_exists,doc_front_exists,expected", [
#     missing_back_document,
#     missing_front_document,
#     missing_both_document,
#     with_all_document,
# ])
# @patch.object(AutoConfig, "__call__")
# @patch.object(FileRepository, "user_file_exists")
# def test_check_document_validator_step_us(
#         mocked_file_repository,
#         mocked_env,
#         doc_back_exists: bool,
#         doc_front_exists: bool,
#         expected: bool
# ):
#     docs_exists = {
#         UserFileType.DOCUMENT_BACK: doc_back_exists,
#         UserFileType.DOCUMENT_FRONT: doc_front_exists,
#     }
#
#     async def aux(file_type, **kwargs):
#         return docs_exists.get(file_type)
#
#     mocked_file_repository.side_effect = aux
#     response = OnboardingUS._check_document_validator_step_us(dummy_missing_steps_user)
#     assert response == expected
#
#
# @patch.object(OnboardingUS, "_check_document_validator_step_us", return_value=False)
# def test_user_document_validator_step_us(mocked_document_checker):
#     response = OnboardingUS._user_document_validator_step_us(dummy_complete_user)
#     mocked_document_checker.assert_called_once_with(dummy_complete_user)
#     assert response is True
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_is_politically_exposed_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._is_politically_exposed_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_is_exchange_member_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._is_exchange_member_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_is_company_director_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._is_company_director_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_external_fiscal_tax_confirmation_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._external_fiscal_tax_confirmation_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_employ_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._employ_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("user,stopped_in_step", [
#     ({"portfolios": {"default": {}}, "external_exchange_requirements": {"us": {"time_experience": True}}}, True),
#     ({"portfolios": {"default": {"us": {"dw_id": dummy_unique_id}}}}, True),
#     (dummy_missing_steps_user, True),
#     (dummy_complete_user, False),
# ])
# def test_time_experience_step(user: dict, stopped_in_step: bool):
#     response = OnboardingUS._time_experience_step(user)
#     assert response == stopped_in_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_w8_confirmation_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingUS._w8_confirmation_step(current_user)
#     assert response == stopped_in_this_step
