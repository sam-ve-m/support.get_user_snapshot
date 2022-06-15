class UserBlocksSnapshotRepository:
    @staticmethod
    def snapshot(user_data: dict) -> dict:
        blocks = {
            "Tipo de bloqueio": None,
            "Descrição": None,
            "Data e Hora": None,
            "Numero do Processo (Caso bloqueio judicial)": None,
        }
        return blocks
