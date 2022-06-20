class UserBlocksSnapshotRepository:
    @staticmethod
    def snapshot(user_data: dict) -> dict:
        blocks = {
            "Tipo de bloqueio": "Pendente de Definição",
            "Descrição": "Pendente de Definição",
            "Data e Hora": "Pendente de Definição",
            "Numero do Processo (Caso bloqueio judicial)": "Pendente de Definição",
        }
        return blocks
