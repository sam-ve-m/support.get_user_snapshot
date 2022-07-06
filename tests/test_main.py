# # Standards
# from http import HTTPStatus
#
# # Third party
# from etria_logger import Gladsheim
# from unittest.mock import patch
# from werkzeug.local import LocalProxy
#
# # Jormungandr
# from func.main import get_user_snapshot
# from func.src.domain.enums import CodeResponse
# from func.src.domain.exceptions import InvalidJwtToken
# from func.src.domain.response.model import ResponseModel
# from func.src.services.jwt.service import JwtService
# from func.src.services.snapshot_builder.service import SnapshotBuilderService
#
# dummy_jwt = "jwt"
# dummy_decoded_jwt = "jwt"
# stub_snapshot = "snapshot"
# dummy_response_model = "response_model"
# dummy_model = "model"
#
#
# @patch.object(JwtService, "apply_authentication_rules")
# @patch.object(JwtService, "decode_jwt", return_value=dummy_decoded_jwt)
# @patch.object(SnapshotBuilderService, "snapshot_user_data", return_value=stub_snapshot)
# @patch.object(ResponseModel, "build_response", return_value=dummy_response_model)
# @patch.object(ResponseModel, "build_error_response")
# @patch.object(ResponseModel, "build_http_response", return_value=dummy_model)
# @patch.object(LocalProxy, "__init__")
# def test_get_user_snapshot(
#         mocked_requests,
#         mocked_build_http_response,
#         mocked_build_error_response,
#         mocked_build_response,
#         mocked_snapshot_user_data,
#         mocked_decode_jwt,
#         mocked_apply_authentication_rules,
#         monkeypatch
# ):
#     setattr(LocalProxy, "headers", {"x-thebes-answer": dummy_jwt})
#     response = get_user_snapshot()
#     mocked_apply_authentication_rules.assert_called_with(jwt=dummy_jwt)
#     mocked_decode_jwt.assert_called_with(jwt=dummy_jwt)
#     mocked_snapshot_user_data.assert_called_with(decoded_jwt=dummy_decoded_jwt)
#     mocked_build_response.assert_called_with(result=stub_snapshot, code=CodeResponse.SUCCESS)
#     mocked_build_error_response.assert_not_called()
#     mocked_build_http_response.assert_called_with(response_model=dummy_response_model, status=HTTPStatus.OK)
#     assert response == dummy_model
#
#
# dummy_invalid_jwt_exception = InvalidJwtToken()
# dummy_invalid_jwt_exception_message = 'Failed to validate user credentials'
# dummy_invalid_jwt_message = "Jormungandr::get_user_snapshot::Invalid JWT token"
#
#
# @patch.object(JwtService, "apply_authentication_rules", side_effect=dummy_invalid_jwt_exception)
# @patch.object(ResponseModel, "build_response")
# @patch.object(Gladsheim, "error")
# @patch.object(ResponseModel, "build_error_response", return_value=dummy_response_model)
# @patch.object(ResponseModel, "build_http_response", return_value=dummy_model)
# @patch.object(LocalProxy, "__init__")
# def test_get_user_snapshot_invalid_jwt(
#         mocked_requests,
#         mocked_build_http_response,
#         mocked_build_error_response,
#         mocked_logger,
#         mocked_build_response,
#         mocked_apply_authentication_rules,
#         monkeypatch
# ):
#     setattr(LocalProxy, "headers", {"x-thebes-answer": dummy_jwt})
#     response = get_user_snapshot()
#     mocked_apply_authentication_rules.assert_called_with(jwt=dummy_jwt)
#     mocked_build_response.assert_not_called()
#     mocked_logger.assert_called_with(error=dummy_invalid_jwt_exception, message=dummy_invalid_jwt_message)
#     mocked_build_error_response.assert_called_with(code=CodeResponse.JWT_INVALID,
#                                                    message=dummy_invalid_jwt_exception_message)
#     mocked_build_http_response.assert_called_with(response_model=dummy_response_model, status=HTTPStatus.UNAUTHORIZED)
#     assert response == dummy_model
#
#
# dummy_common_exception = Exception()
# dummy_common_exception_message = "Unexpected error occurred"
# dummy_common_message = "Jormungandr::get_user_snapshot::"
#
#
# @patch.object(JwtService, "apply_authentication_rules")
# @patch.object(JwtService, "decode_jwt", return_value=dummy_decoded_jwt)
# @patch.object(SnapshotBuilderService, "snapshot_user_data", side_effect=dummy_common_exception)
# @patch.object(ResponseModel, "build_response")
# @patch.object(Gladsheim, "error")
# @patch.object(ResponseModel, "build_error_response", return_value=dummy_response_model)
# @patch.object(ResponseModel, "build_http_response", return_value=dummy_model)
# @patch.object(LocalProxy, "__init__")
# def test_get_user_snapshot_execution_error(
#         mocked_requests,
#         mocked_build_http_response,
#         mocked_build_error_response,
#         mocked_logger,
#         mocked_build_response,
#         mocked_snapshot_user_data,
#         mocked_decode_jwt,
#         mocked_apply_authentication_rules,
#         monkeypatch
# ):
#     setattr(LocalProxy, "headers", {"x-thebes-answer": dummy_jwt})
#     response = get_user_snapshot()
#     mocked_apply_authentication_rules.assert_called_with(jwt=dummy_jwt)
#     mocked_decode_jwt.assert_called_with(jwt=dummy_jwt)
#     mocked_snapshot_user_data.assert_called_with(decoded_jwt=dummy_decoded_jwt)
#     mocked_build_response.assert_not_called()
#     mocked_logger.assert_called_with(error=dummy_common_exception, message=dummy_common_message)
#     mocked_build_error_response.assert_called_with(code=CodeResponse.INTERNAL_SERVER_ERROR,
#                                                    message=dummy_common_exception_message)
#     mocked_build_http_response.assert_called_with(response_model=dummy_response_model,
#                                                   status=HTTPStatus.INTERNAL_SERVER_ERROR)
#     assert response == dummy_model
#


# # Jormungandr
# from unittest.mock import MagicMock
#
# import pytest
#
# from func.src.repository.user.repository import UserRepository
# from unittest.mock import patch
#
# from func.src.services.snapshot_builder.service import SnapshotBuilderService
#
# dummy_decoded_jwt = {"user": {"unique_id": "159951"}}
# dummy_user = {"some": "value"}
# mocked_pid = MagicMock()
# mocked_onboarding_repo = MagicMock()
# mocked_wallet = MagicMock()
# mocked_vai_na_cola = MagicMock()
# mocked_blocked_assets = MagicMock()
# mocked_user_blocks = MagicMock()
# mocked_warranty_assets = MagicMock()
# mocked_warranty = MagicMock()
#
#
# def test_snapshot_user_data(monkeypatch):
#     monkeypatch.setattr(
#         SnapshotBuilderService,
#         "user_repository",
#         MagicMock(find_user_by_unique_id=MagicMock(return_value=dummy_user))
#     )
#     monkeypatch.setattr(SnapshotBuilderService, "pid_model", mocked_pid)
#     monkeypatch.setattr(SnapshotBuilderService, "onboarding_model", mocked_onboarding_repo)
#     monkeypatch.setattr(SnapshotBuilderService, "wallet_model", mocked_wallet)
#     monkeypatch.setattr(SnapshotBuilderService, "vai_na_cola_model", mocked_vai_na_cola)
#     monkeypatch.setattr(SnapshotBuilderService, "blocked_assets_model", mocked_blocked_assets)
#     monkeypatch.setattr(SnapshotBuilderService, "user_blocks_model", mocked_user_blocks)
#     monkeypatch.setattr(SnapshotBuilderService, "warranty_assets_model", mocked_warranty_assets)
#     monkeypatch.setattr(SnapshotBuilderService, "warranty_model", mocked_warranty)
#     SnapshotBuilderService.snapshot_user_data(dummy_decoded_jwt)
#     mocked_pid.assert_called_once_with(dummy_user)
#     mocked_pid.return_value.get_snapshot.assert_called_once_with()
#     mocked_onboarding_repo.assert_called_once_with(dummy_user)
#     mocked_onboarding_repo.return_value.get_snapshot.assert_called_once_with()
#     mocked_wallet.assert_called_once_with(dummy_user)
#     mocked_wallet.return_value.get_snapshot.assert_called_once_with()
#     mocked_vai_na_cola.assert_called_once_with(dummy_user)
#     mocked_vai_na_cola.return_value.get_snapshot.assert_called_once_with()
#     mocked_blocked_assets.assert_called_once_with(dummy_user)
#     mocked_blocked_assets.return_value.get_snapshot.assert_called_once_with()
#     mocked_user_blocks.assert_called_once_with(dummy_user)
#     mocked_user_blocks.return_value.get_snapshot.assert_called_once_with()
#     mocked_warranty_assets.assert_called_once_with(dummy_user)
#     mocked_warranty_assets.return_value.get_snapshot.assert_called_once_with()
#     mocked_warranty.assert_called_once_with(dummy_user)
#     mocked_warranty.return_value.get_snapshot.assert_called_once_with()
#
#
# @patch.object(UserRepository, "find_user_by_unique_id", return_value=False)
# def test_snapshot_user_data_no_user(monkeypatch):
#     with pytest.raises(ValueError):
#         SnapshotBuilderService.snapshot_user_data(dummy_decoded_jwt)
