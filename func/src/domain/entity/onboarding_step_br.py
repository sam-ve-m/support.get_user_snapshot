from func.src.domain.enums import CAFStatus


class OnboardingBR:
    @staticmethod
    def user_suitability_step(current_user: dict):
        has_signed_suitability = bool(current_user.get("suitability"))
        has_signed_refusal_term = current_user.get("terms", {}).get("term_refusal") is not None
        stopped_in_suitability = not has_signed_suitability and not has_signed_refusal_term
        return stopped_in_suitability

    @staticmethod
    def user_identifier_step(current_user: dict):
        user_cpf = current_user.get("identifier_document", {}).get("cpf")
        user_cel_phone = current_user.get("phone")
        stopped_in_identification = user_cpf is None and user_cel_phone is None
        return stopped_in_identification

    @staticmethod
    def user_selfie_step(check_if_selfie_exists_callback: callable):
        return not check_if_selfie_exists_callback()

    @staticmethod
    def user_complementary_step(current_user: dict):
        marital = current_user.get("marital")
        stopped_in_marital_identification = marital is None
        return stopped_in_marital_identification

    @classmethod
    def user_document_validator_step_br(cls, current_user: dict, check_if_document_exists_callback: callable):
        if current_user.get("bureau_status") == CAFStatus.DOCUMENT.value:
            return not check_if_document_exists_callback()

    @staticmethod
    def user_data_validation_step(current_user: dict):
        has_validate_data = current_user.get("is_bureau_data_validated")
        stopped_in_data_validation = not has_validate_data
        return stopped_in_data_validation

    @staticmethod
    def user_electronic_signature_step(current_user: dict):
        has_electronic_signature = current_user.get("electronic_signature")
        stopped_in_electronic_signature_creation = not has_electronic_signature
        return stopped_in_electronic_signature_creation

