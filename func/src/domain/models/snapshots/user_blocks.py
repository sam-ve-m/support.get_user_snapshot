class UserBlocks:
    def __init__(self, user_data: dict):
        self.__block_type = "Pendente de Definição"
        self.__description = "Pendente de Definição"
        self.__date = "Pendente de Definição"
        self.__lawsuit_number = "Pendente de Definição"

    def get_snapshot(self) -> list:
        snapshot = [
            {"value": self.__block_type, "label": "Tipo de bloqueio"},
            {"value": self.__description, "label": "Descrição"},
            {"value": self.__date, "label": "Data e Hora"},
            {"value": self.__lawsuit_number, "label": "Numero do Processo (Caso bloqueio judicial)"},
        ]
        return snapshot
