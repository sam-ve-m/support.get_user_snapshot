from func.src.domain.validator import WarrantySummary


class Warranty:
    def __init__(self, warranty_summary: WarrantySummary):
        self.__warranty_available = warranty_summary.available

    def get_snapshot(self) -> list:
        snapshot = [
            {"value": self.__warranty_available, "label": "Disponível em Garantia"},
        ]
        return snapshot
