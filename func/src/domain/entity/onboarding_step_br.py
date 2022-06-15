import asyncio

from decouple import config

from func.src.domain.enums import UserFileType, CAFStatus
from func.src.repository.file.repository import FileRepository


class OnboardingBR:
    _steps_br = {
        "_user_suitability_step": "Assinar o Suitability",
        "_user_identifier_step": "Informar CPF e Telefone",
        "_user_selfie_step": "Tirar a Selfie",
        "_user_complementary_step": "Informar dados complementares",
        "_user_document_validator_step_br": "Tirar foto do Documento",
        "_user_data_validation_step": "O Birô analisar os dados",
        "_user_electronic_signature_step": "Criar uma ssinatura eletrônica",
    }

    @classmethod
    def find_missing_step(cls, user_data: dict):
        if user_data.get('portfolios', {}).get('default', {}).get("br", {}).get("bovespa_account"):
            return "Nada"

        for step, label in cls._steps_br.items():
            stopped_in_this_step = getattr(cls, step)
            if stopped_in_this_step(user_data):
                return label
        return "Nada"

    @staticmethod
    def _user_suitability_step(current_user: dict):
        has_signed_suitability = bool(current_user.get("suitability"))
        terms = current_user.get("terms")
        has_signed_refusal_term = terms.get("term_refusal") is not None
        stopped_in_suitability = not has_signed_suitability and not has_signed_refusal_term
        return stopped_in_suitability

    @staticmethod
    def _user_identifier_step(current_user: dict):
        user_cpf = current_user.get("identifier_document", {}).get("cpf")
        user_cel_phone = current_user.get("phone")
        stopped_in_identification = user_cpf is None and user_cel_phone is None
        return stopped_in_identification

    @classmethod
    def _check_if_selfie_exists(cls, current_user: dict) -> bool:
        return asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.SELFIE,
            unique_id=current_user.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        ))

    @classmethod
    def _user_selfie_step(cls, current_user: dict):
        return not cls._check_if_selfie_exists(current_user)

    @staticmethod
    def _user_complementary_step(current_user: dict):
        marital = current_user.get("marital")
        stopped_in_marital_identification = marital is None
        return stopped_in_marital_identification

    @classmethod
    def _check_document_validator_step_br(cls, current_user: dict) -> bool:
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
    def _user_document_validator_step_br(cls, current_user: dict):
        if current_user.get("bureau_status") == CAFStatus.DOCUMENT.value:
            return not cls._check_document_validator_step_br(current_user)

    @staticmethod
    def _user_data_validation_step(current_user: dict):
        has_validate_data = current_user.get("is_bureau_data_validated")
        stopped_in_data_validation = not has_validate_data
        return stopped_in_data_validation

    @staticmethod
    def _user_electronic_signature_step(current_user: dict):
        has_electronic_signature = current_user.get("electronic_signature")
        stopped_in_electronic_signature_creation = not has_electronic_signature
        return stopped_in_electronic_signature_creation

