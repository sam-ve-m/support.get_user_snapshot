class WarrantyAssetsSnapshotRepository:
    @staticmethod
    def snapshot(user_data: dict) -> list:
        warrant = [{
            "Ativo": "Pendente de Definição",
            "Valor": "Pendente de Definição",
            "Quantidade": "Pendente de Definição"
        }] * 3
        return warrant

