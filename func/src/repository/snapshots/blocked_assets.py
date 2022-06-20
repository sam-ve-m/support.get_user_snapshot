class BlockedAssetsSnapshotRepository:
    @staticmethod
    def snapshot(user_data: dict) -> list:
        blocks = [{
            "Ativo": "Pendente de Definição",
            "Preço Médio": "Pendente de Definição",
            "Quantidade": "Pendente de Definição"
        }]*3
        return blocks
