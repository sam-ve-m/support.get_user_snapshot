from func.src.domain.enums import TermsFileType


class OnboardingUS:
    @staticmethod
    def terms_step(current_user: dict):
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

    @staticmethod
    def user_document_validator_step_us(check_if_document_exists_callback: callable):
        return not check_if_document_exists_callback()

    @staticmethod
    def is_politically_exposed_step(current_user: dict):
        politically_exposed = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_politically_exposed")
        )
        stopped_in_political_exposed_step = politically_exposed is None
        return stopped_in_political_exposed_step

    @staticmethod
    def is_exchange_member_step(current_user: dict):
        is_exchange_member = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_exchange_member")
        )
        stopped_in_exchange_member_step = is_exchange_member is None
        return stopped_in_exchange_member_step

    @staticmethod
    def is_company_director_step(current_user: dict):
        is_company_director = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("is_company_director")
        )
        stopped_in_company_director_step = is_company_director is None
        return stopped_in_company_director_step

    @staticmethod
    def external_fiscal_tax_confirmation_step(current_user: dict):
        fiscal_tax_confirmation = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("external_fiscal_tax_confirmation")
        )
        stopped_in_fiscal_tax_confirmation_step = not fiscal_tax_confirmation
        return stopped_in_fiscal_tax_confirmation_step

    @staticmethod
    def employ_step(current_user: dict):
        user_employ_status = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("user_employ_status")
        )
        stopped_in_user_employ_status_step = not user_employ_status
        return stopped_in_user_employ_status_step

    @staticmethod
    def time_experience_step(current_user: dict):
        is_time_experience_filled = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("time_experience")
        )
        user_was_created_on_dw = current_user["portfolios"]["default"].get("us", {}).get("dw_id")
        stopped_in_time_experience_step = is_time_experience_filled is None or user_was_created_on_dw is None
        return stopped_in_time_experience_step

    @staticmethod
    def w8_confirmation_step(current_user: dict):
        has_w8_confirmation = (
            current_user.get("external_exchange_requirements", {})
            .get("us", {})
            .get("w8_confirmation")
        )
        return not has_w8_confirmation
