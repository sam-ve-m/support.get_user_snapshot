class Warranty:
    def __init__(self, user_data: dict):
        self.__warranty_available = "Pendente de Definição"

    def get_snapshot(self) -> list:
        snapshot = [
            {"value": self.__warranty_available, "label": "Disponível em Garantia"},
        ]
        return snapshot
