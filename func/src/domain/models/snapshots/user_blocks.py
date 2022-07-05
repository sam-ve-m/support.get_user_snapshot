from func.src.domain.validator import BlockSummary


class UserBlocks:
    def __init__(self, block_summary: BlockSummary):
        self.__block_type = block_summary.block_type
        self.__description = block_summary.description
        self.__date = block_summary.date
        self.__lawsuit_number = block_summary.lawsuit_number

    def get_snapshot(self) -> list:
        snapshot = [
            {"value": self.__block_type, "label": "Tipo de bloqueio"},
            {"value": self.__description, "label": "Descrição"},
            {"value": self.__date, "label": "Data e Hora"},
            {"value": self.__lawsuit_number, "label": "Numero do Processo (Caso bloqueio judicial)"},
        ]
        return snapshot
