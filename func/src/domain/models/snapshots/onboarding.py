from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.entity.onboarding_step_us import OnboardingUS


class Onboarding:
    def __init__(self, user_data: dict):
        self.__missed_steps_br = OnboardingBR.find_missing_step(user_data)
        self.__date_br = "??/??/????"
        self.__missed_steps_us = OnboardingUS.find_missing_step(user_data)
        self.__date_us = "??/??/????"

    def __normalize_missed_steps(self) -> list:
        missed_steps = [
            {"value": "Faltou fazer", "label": "Campo"},
            {"value": self.__missed_steps_br, "label": "BR"},
            {"value": self.__missed_steps_us, "label": "US"},
        ]
        return missed_steps

    def __normalize_dates(self) -> list:
        dates = [
            {"value": "Data da Ultima", "label": "Campo"},
            {"value": self.__date_br, "label": "BR"},
            {"value": self.__date_us, "label": "US"},
        ]
        return dates

    def get_snapshot(self) -> list:
        snapshot = [
            self.__normalize_missed_steps(),
            self.__normalize_dates(),
        ]
        return snapshot

