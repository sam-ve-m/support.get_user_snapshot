import asyncio

from decouple import config

from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.enums import UserFileType
from func.src.repository.file.repository import FileRepository
from func.src.services.base.missing_steps import BaseGetMissingStep


class GetMissingStepBR(BaseGetMissingStep):
    _steps_labels = {
        1: "Assinar o Suitability",
        2: "Informar CPF e Telefone",
        3: "Tirar a Selfie",
        4: "Informar dados complementares",
        5: "Tirar foto do Documento",
        6: "O Birô analisar os dados",
        7: "Criar uma ssinatura eletrônica",
    }

    def _get_steps(self) -> dict:
        steps = {
            1: lambda: OnboardingBR.user_suitability_step(self._user_data),
            2: lambda: OnboardingBR.user_identifier_step(self._user_data),
            3: lambda: OnboardingBR.user_selfie_step(self._check_if_selfie_exists),
            4: lambda: OnboardingBR.user_complementary_step(self._user_data),
            5: lambda: OnboardingBR.user_document_validator_step_br(self._user_data,
                                                                    self._check_document_validator_step_br),
            6: lambda: OnboardingBR.user_data_validation_step(self._user_data),
            7: lambda: OnboardingBR.user_electronic_signature_step(self._user_data),
        }
        return steps

    def _nothing_is_missing(self) -> bool:
        nothing_is_missing = bool(self._user_data.get('portfolios', {}).get('default', {}).get("br", {}).get("bovespa_account"))
        return nothing_is_missing

    def _check_if_selfie_exists(self) -> bool:
        return asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.SELFIE,
            unique_id=self._user_data.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        ))

    def _check_document_validator_step_br(self) -> bool:
        return asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_BACK,
            unique_id=self._user_data.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        )) and asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_FRONT,
            unique_id=self._user_data.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        ))
