# Standards
from http import HTTPStatus

# Third party
from etria_logger import Gladsheim
from flask import request

# Jormungandr
from func.src.services.jwt import JwtService
from func.src.domain.enums import CodeResponse
from func.src.domain.exceptions import InvalidJwtToken
from func.src.domain.response.model import ResponseModel
from func.src.services.get_user_snapshot import GetUserSnapshotService


def get_user_snapshot():
    message = "Jormungandr::get_user_snapshot"
    jwt = request.headers.get("x-thebes-answer")
    try:
        JwtService.apply_authentication_rules(jwt=jwt)
        decoded_jwt = JwtService.decode_jwt(jwt=jwt)
        snapshots = GetUserSnapshotService.snapshot_user_data(decoded_jwt=decoded_jwt)
        response_model = ResponseModel.build_response(
            result=snapshots,
            code=CodeResponse.SUCCESS,
        )

        response = ResponseModel.build_http_response(
            response_model=response_model,
            status=HTTPStatus.OK
        )
        return response

    except InvalidJwtToken as ex:
        Gladsheim.error(error=ex, message=f"{message}::Invalid JWT token")
        response_model = ResponseModel.build_error_response(
            code=CodeResponse.JWT_INVALID,
            message=ex.msg,
        )
        response = ResponseModel.build_http_response(
            response_model=response_model,
            status=HTTPStatus.UNAUTHORIZED
        )
        return response

    except ValueError as ex:
        Gladsheim.error(ex=ex, message=f'{message}::There are invalid format or extra parameters')
        response_model = ResponseModel.build_error_response(
            code=CodeResponse.INVALID_PARAMS,
            message="There are invalid format or extra/missing parameters",
        )
        response = ResponseModel.build_http_response(
            response_model=response_model,
            status=HTTPStatus.BAD_REQUEST
        )
        return response

    except Exception as ex:
        Gladsheim.error(error=ex, message=f"{message}::{str(ex)}")
        response_model = ResponseModel.build_error_response(
            code=CodeResponse.INTERNAL_SERVER_ERROR,
            message="Unexpected error occurred",
        )
        response = ResponseModel.build_http_response(
            response_model=response_model,
            status=HTTPStatus.INTERNAL_SERVER_ERROR
        )
        return response
