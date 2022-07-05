class Onboarding:
    def __init__(
            self,
            missed_steps_br: str,
            date_of_missed_steps_br: str,
            missed_steps_us: str,
            date_of_missed_steps_us: str
    ):
        self.__missed_steps_br = missed_steps_br
        self.__date_br = date_of_missed_steps_br
        self.__missed_steps_us = missed_steps_us
        self.__date_us = date_of_missed_steps_us

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

