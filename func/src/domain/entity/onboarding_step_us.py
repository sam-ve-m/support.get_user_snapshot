import asyncio

from decouple import config

from func.src.domain.enums import UserFileType, TermsFileType
from func.src.repository.file.repository import FileRepository


class OnboardingUS:

    _steps_us = {
        "_terms_step": "Assinar os Termos",
        "_user_document_validator_step_us": "Enviar Documento",
        "_is_politically_exposed_step": "Informar se é PEP",
        "_is_exchange_member_step": "Informar se é exchange_member",
        "_is_company_director_step": "Informar se é Diretor",
        "_external_fiscal_tax_confirmation_step": "Confirmar residencia fiscal",
        "_employ_step": "Informar emprego",
        "_time_experience_step": "Informar tempo de experiência",
        "_w8_confirmation_step": "Confirmar o W8",
    }

    @classmethod
    def find_missing_step(cls, user_data: dict):
        if user_data.get('portfolios', {}).get('default', {}).get("us", {}).get("dw_account"):
            return "Nada"

        for step, label in cls._steps_us.items():
            stopped_in_this_step = getattr(cls, step)
            if stopped_in_this_step(user_data):
                return label
        return "Nada"

    @staticmethod
    def _terms_step(current_user: dict):
        user_terms = current_user.get("terms", {})
        terms_that_needs_be_signed = {
            TermsFileType.TERM_OPEN_ACCOUNT_DW,
            TermsFileType.TERM_APPLICATION_DW,
            TermsFileType.TERM_PRIVACY_POLICY_AND_DATA_SHARING_POLICY_DW,
            TermsFileType.TERM_DISCLOSURES_AND_DISCLAIMERS,
            TermsFileType.TERM_MONEY_CORP,
            TermsFileType.TERM_GRINGO_WORLD,
            TermsFileType.TERM_GRINGO_WORLD_GENERAL_ADVICES,
        }
        has_signed_terms = all(user_terms.get(term.value) for term in terms_that_needs_be_signed)
        return not has_signed_terms

    @classmethod
    def _check_document_validator_step_us(cls, current_user: dict) -> bool:
        return asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_BACK,
            unique_id=current_user.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        )) and asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_FRONT,
            unique_id=current_user.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        ))

    @classmethod
    def _user_document_validator_step_us(cls, current_user: dict):
        return not cls._check_document_validator_step_us(current_user)

    @staticmethod
    def _is_politically_exposed_step(current_user: dict):
        politically_exposed = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_politically_exposed")
        )
        stopped_in_political_exposed_step = politically_exposed is None
        return stopped_in_political_exposed_step

    @staticmethod
    def _is_exchange_member_step(current_user: dict):
        is_exchange_member = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_exchange_member")
        )
        stopped_in_exchange_member_step = is_exchange_member is None
        return stopped_in_exchange_member_step

    @staticmethod
    def _is_company_director_step(current_user: dict):
        is_company_director = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_company_director")
        )
        stopped_in_company_director_step = is_company_director is None
        return stopped_in_company_director_step

    @staticmethod
    def _external_fiscal_tax_confirmation_step(current_user: dict):
        fiscal_tax_confirmation = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("external_fiscal_tax_confirmation")
        )
        stopped_in_fiscal_tax_confirmation_step = not fiscal_tax_confirmation
        return stopped_in_fiscal_tax_confirmation_step

    @staticmethod
    def _employ_step(current_user: dict):
        user_employ_status = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("user_employ_status")
        )
        stopped_in_user_employ_status_step = not user_employ_status
        return stopped_in_user_employ_status_step

    @staticmethod
    def _time_experience_step(current_user: dict):
        is_time_experience_filled = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("time_experience")
        )
        user_was_created_on_dw = current_user["portfolios"]["default"].get("us", {}).get("dw_id")
        stopped_in_time_experience_step = is_time_experience_filled is None or user_was_created_on_dw is None
        return stopped_in_time_experience_step

    @staticmethod
    def _w8_confirmation_step(current_user: dict):
        has_w8_confirmation = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("w8_confirmation")
        )
        return not has_w8_confirmation
