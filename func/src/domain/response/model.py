# Jormungandr
from ..validator import Snapshots
from ...domain.enums import CodeResponse

# Standards
from json import dumps

# Third party
from flask import Response
from nidavellir import Sindri


class ResponseModel:
    @staticmethod
    def build_response(result: Snapshots, code: CodeResponse) -> str:
        response_model = dumps(
            {
                "result": result.dict(),
                "code": code.value,
            },
            default=Sindri.resolver,
        )
        return response_model

    @staticmethod
    def build_error_response(message: str, code: CodeResponse) -> str:
        response_model = dumps(
            {
                "message": message,
                "code": code.value,
            },
            default=Sindri.resolver,
        )
        return response_model

    @staticmethod
    def build_http_response(response_model: str, status: int, mimetype: str = "application/json") -> Response:
        response = Response(
            response_model,
            mimetype=mimetype,
            status=status.value,
        )
        return response
