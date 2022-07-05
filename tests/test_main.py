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
