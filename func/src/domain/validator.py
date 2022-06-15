from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.entity.onboarding_step_us import OnboardingUS
from pydantic import BaseModel


class Snapshots(BaseModel):
    pid: dict
    onboarding: list
    wallet: list
    vai_na_cola: list
    blocked_assets: list
    user_blocks: dict
    warranty_assets: list
    warranty: dict


class Onboarding:
    user_data: dict
    missing_step_br: str
    missing_step_us: str

    def __init__(self, user_data: dict):
        self.missing_step_br = OnboardingBR.find_missing_step(user_data)
        self.missing_step_us = OnboardingUS.find_missing_step(user_data)
        self.user_data = user_data
