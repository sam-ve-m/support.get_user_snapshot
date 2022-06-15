# Standards
from enum import Enum, IntEnum


class CodeResponse(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    PARTNERS_INVALID_API_URL = 20
    PARTNERS_ERROR_ON_API_REQUEST = 21
    JWT_INVALID = 30
    DATA_NOT_FOUND = 99
    INTERNAL_SERVER_ERROR = 100


class CAFStatus(Enum):
    APPROVED = "approved"
    DOCUMENT = "document"
    REFUSED = "refused"


class UserFileType(Enum):
    SELFIE = "user_selfie"
    DOCUMENT_BACK = "document_back"
    DOCUMENT_FRONT = "document_front"


class TermsFileType(Enum):
    TERM_APPLICATION = "term_application"
    TERM_OPEN_ACCOUNT = "term_open_account"
    TERM_REFUSAL = "term_refusal"
    TERM_NON_COMPLIANCE = "term_non_compliance"
    TERM_RETAIL_LIQUID_PROVIDER = "term_retail_liquid_provider"

    TERM_OPEN_ACCOUNT_DW = "term_open_account_dw"
    TERM_APPLICATION_DW = "term_application_dw"
    TERM_PRIVACY_POLICY_AND_DATA_SHARING_POLICY_DW = "term_and_privacy_policy_data_sharing_policy_dw"
    TERM_DISCLOSURES_AND_DISCLAIMERS = "term_disclosures_and_disclaimers"
    TERM_MONEY_CORP = "term_money_corp"
    TERM_GRINGO_WORLD = "term_gringo_world"
    TERM_GRINGO_WORLD_GENERAL_ADVICES = "term_gringo_world_general_advices"
