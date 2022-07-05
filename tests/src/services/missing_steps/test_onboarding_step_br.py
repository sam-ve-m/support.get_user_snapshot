# from unittest.mock import patch
#
# import pytest
# from decouple import AutoConfig
#
# from func.src.domain.entity.onboarding_step_br import OnboardingBR
# from func.src.domain.enums import UserFileType, CAFStatus
# from func.src.repository.file.repository import FileRepository
#
# dummy_unique_id = "15619584"
# dummy_complete_user = {
#     "portfolios": {"default": {"br": {"bovespa_account": dummy_unique_id}}},
#     "unique_id": dummy_unique_id,
#     "suitability": {"suit": "ability"},
#     "terms": {"term_refusal": False},
#     "identifier_document": {"cpf": True},
#     "phone": True,
#     "marital": True,
#     "bureau_status": CAFStatus.APPROVED.value,
#     "is_bureau_data_validated": True,
#     "electronic_signature": True,
# }
# dummy_missing_steps_user = {
#     "portfolios": {"default": {"br": {"bovespa_account": None}}},
#     "unique_id": dummy_unique_id,
#     "suitability": None,
#     # "terms": None,
#     # "identifier_document": None,
#     "phone": None,
#     "marital": None,
#     "bureau_status": CAFStatus.DOCUMENT.value,
#     "is_bureau_data_validated": False,
#     "electronic_signature": False
# }
#
#
# def test_find_missing_step_has_bovespa_account():
#     response = OnboardingBR.find_missing_step(dummy_complete_user)
#     assert response == "Nada"
#
#
# fake_func = "_fake_function"
# dummy_missing_step_label = "Label"
# fake_missing_steps_br = {
#     fake_func: dummy_missing_step_label
# }
#
#
# def test_find_missing_step_has_missing_step(monkeypatch):
#     monkeypatch.setattr(OnboardingBR, "_steps_br", fake_missing_steps_br)
#     setattr(OnboardingBR, fake_func, lambda x: True)
#     response = OnboardingBR.find_missing_step(dummy_missing_steps_user)
#     assert response == dummy_missing_step_label
#
#
# fake_complete_steps_br = {
#     fake_func: dummy_missing_step_label
# }
#
#
# def test_find_missing_step_no_missing_step(monkeypatch):
#     monkeypatch.setattr(OnboardingBR, "_steps_br", fake_complete_steps_br)
#     setattr(OnboardingBR, fake_func, lambda x: False)
#     response = OnboardingBR.find_missing_step(dummy_missing_steps_user)
#     assert response == "Nada"
#
#
# @pytest.mark.parametrize("user,stopped_in_step", [
#     ({"suitability": {"suit": "ability"}}, False),
#     ({"terms": {"term_refusal": False}}, False),
#     (dummy_missing_steps_user, True),
#     (dummy_complete_user, False),
# ])
# def test_user_suitability_step(user: dict, stopped_in_step: bool):
#     response = OnboardingBR._user_suitability_step(user)
#     assert response is stopped_in_step
#
#
# @pytest.mark.parametrize("user,stopped_in_step", [
#     ({"identifier_document": {"cpf": True}}, False),
#     (dummy_missing_steps_user, True),
#     (dummy_complete_user, False),
#     ({"phone": True}, False),
# ])
# def test_user_identifier_step(user: dict, stopped_in_step: bool):
#     response = OnboardingBR._user_identifier_step(user)
#     assert response is stopped_in_step
#
#
# @patch.object(AutoConfig, "__call__", return_value=True)
# @patch.object(FileRepository, "user_file_exists", return_value=True)
# def test_check_if_selfie_exists(mocked_file_repository, mocked_env):
#     response = OnboardingBR._check_if_selfie_exists(dummy_complete_user)
#     mocked_file_repository.assert_called_once_with(
#         file_type=UserFileType.SELFIE,
#         unique_id=dummy_unique_id,
#         bucket_name=True,
#     )
#     assert response is True
#
#
# @patch.object(OnboardingBR, "_check_if_selfie_exists", return_value=True)
# def test_user_selfie_step(mocked_selfie_checker):
#     response = OnboardingBR._user_selfie_step(dummy_complete_user)
#     mocked_selfie_checker.assert_called_once_with(dummy_complete_user)
#     assert response is False
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_user_complementary_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingBR._user_complementary_step(current_user)
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
# def test_check_document_validator_step_br(
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
#     response = OnboardingBR._check_document_validator_step_br(dummy_missing_steps_user)
#     assert response == expected
#
#
# def test_user_document_validator_step_br_not_in_document_bureau_status():
#     response = OnboardingBR._user_document_validator_step_br(dummy_complete_user)
#     assert response is None
#
#
# @patch.object(OnboardingBR, "_check_document_validator_step_br", return_value=False)
# def test_user_document_validator_step_br(mocked_doc_validation):
#     response = OnboardingBR._user_document_validator_step_br(dummy_missing_steps_user)
#     mocked_doc_validation.assert_called_once_with(dummy_missing_steps_user)
#     assert response is True
#
#
# def test_user_document_validator_step_br_bureau_validated():
#     response = OnboardingBR._user_document_validator_step_br(dummy_complete_user)
#     assert response is None
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_user_data_validation_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingBR._user_data_validation_step(current_user)
#     assert response == stopped_in_this_step
#
#
# @pytest.mark.parametrize("current_user,stopped_in_this_step", [
#     (dummy_complete_user, False),
#     (dummy_missing_steps_user, True)
# ])
# def test_user_electronic_signature_step(current_user: dict, stopped_in_this_step: bool):
#     response = OnboardingBR._user_electronic_signature_step(current_user)
#     assert response == stopped_in_this_step
