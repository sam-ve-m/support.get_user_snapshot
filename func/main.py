# Standards
from http import HTTPStatus

# Third party
from etria_logger import Gladsheim
from flask import request

# Jormungandr
from func.src.domain.enums import CodeResponse
from func.src.domain.exceptions import InvalidJwtToken
from func.src.domain.response.model import ResponseModel
from func.src.services.jwt.service import JwtService
from func.src.services.blocks.service import BlockService
from func.src.services.get_user_data.service import GetUserDataService
from func.src.services.missing_steps.service_br import GetMissingStepBR
from func.src.services.missing_steps.service_us import GetMissingStepUS
from func.src.services.portfolio.service import PortfolioService
from func.src.services.snapshot_builder.service import SnapshotBuilderService
from func.src.services.vai_na_cola.service import VaiNaColaService
from func.src.services.warranty.service import WarrantyService


def get_user_snapshot():
    message = "Jormungandr::get_user_snapshot"
    jwt = request.headers.get("x-thebes-answer")
    try:
        JwtService.apply_authentication_rules(jwt=jwt)
        decoded_jwt = JwtService.decode_jwt(jwt=jwt)
        user_data = GetUserDataService.get_user_data(decoded_jwt)
        missed_steps_br = GetMissingStepBR(user_data).get_missing_step()
        missed_steps_us = GetMissingStepUS(user_data).get_missing_step()
        block_summary = BlockService.get_block_summary(user_data)
        blocked_assets = BlockService.get_blocked_wallet(user_data)
        warranty_summary = WarrantyService.get_warranty_summary(user_data)
        warranty_assets = WarrantyService.get_warrantyed_wallet(user_data)
        portfolio = PortfolioService.get_user_portfolio(user_data)
        vnc_portfolio_report = VaiNaColaService.get_vai_na_cola_portfolio_report(portfolio)

        snapshots = (
            SnapshotBuilderService()
            .set_pid(user_data)
            .set_onboarding(missed_steps_br, missed_steps_us)
            .set_wallet(portfolio)
            .set_vai_na_cola(vnc_portfolio_report)
            .set_blocked_assets(blocked_assets)
            .set_user_blocks(block_summary)
            .set_warranty_assets(warranty_assets)
            .set_warranty(warranty_summary)
        ).get_snapshot()

        response_model = ResponseModel.build_response(result=snapshots, code=CodeResponse.SUCCESS)
        response = ResponseModel.build_http_response(response_model=response_model, status=HTTPStatus.OK)
        return response

    except InvalidJwtToken as ex:
        Gladsheim.error(error=ex, message=f"{message}::Invalid JWT token")
        response_model = ResponseModel.build_error_response(code=CodeResponse.JWT_INVALID, message=ex.msg)
        response = ResponseModel.build_http_response(response_model=response_model, status=HTTPStatus.UNAUTHORIZED)
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
