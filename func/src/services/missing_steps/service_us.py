import asyncio

from decouple import config

from func.src.domain.entity.onboarding_step_us import OnboardingUS
from func.src.domain.enums import UserFileType
from func.src.repository.file.repository import FileRepository
from func.src.services.base.missing_steps import BaseGetMissingStep


class GetMissingStepUS(BaseGetMissingStep):
    _steps_labels = {
        1: "Assinar os Termos",
        2: "Enviar Documento",
        3: "Informar se é PEP",
        4: "Informar se é exchange_member",
        5: "Informar se é Diretor",
        6: "Confirmar residencia fiscal",
        7: "Informar emprego",
        8: "Informar tempo de experiência",
        9: "Confirmar o W8",
    }

    def _get_steps(self) -> dict:
        steps = {
            1: lambda: OnboardingUS.terms_step(self._user_data),
            2: lambda: OnboardingUS.user_document_validator_step_us(self._check_document_validator_step_us),
            3: lambda: OnboardingUS.is_politically_exposed_step(self._user_data),
            4: lambda: OnboardingUS.is_exchange_member_step(self._user_data),
            5: lambda: OnboardingUS.is_company_director_step(self._user_data),
            6: lambda: OnboardingUS.external_fiscal_tax_confirmation_step(self._user_data),
            7: lambda: OnboardingUS.employ_step(self._user_data),
            8: lambda: OnboardingUS.time_experience_step(self._user_data),
            9: lambda: OnboardingUS.w8_confirmation_step(self._user_data),
        }
        return steps

    def _nothing_is_missing(self) -> bool:
        nothing_is_missing = bool(self._user_data.get('portfolios', {}).get('default', {}).get("us", {}).get("dw_account"))
        return nothing_is_missing

    def _check_document_validator_step_us(self) -> bool:
        return asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_BACK,
            unique_id=self._user_data.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        )) and asyncio.run(FileRepository.user_file_exists(
            file_type=UserFileType.DOCUMENT_FRONT,
            unique_id=self._user_data.get("unique_id"),
            bucket_name=config("AWS_BUCKET_USERS_FILES"),
        ))

