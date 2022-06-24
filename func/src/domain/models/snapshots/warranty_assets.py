class WarrantyAssets:
    def __init__(self, user_data: dict):
        self.__warranty_assets = self._request_blocked_assets(user_data)

    def _request_blocked_assets(self, user_data: dict) -> list:
        warranty_assets = [{}, {}, {}]
        return warranty_assets

    @staticmethod
    def __normalize_assets(asset: dict) -> list:
        normalized_asset = [
            {"value": "Pendente de Definição", "label": "Ativo"},
            {"value": "Pendente de Definição", "label": "Valor"},
            {"value": "Pendente de Definição", "label": "Quantidade"},
        ]
        return normalized_asset

    def get_snapshot(self) -> list:
        snapshot = [self.__normalize_assets(asset) for asset in self.__warranty_assets]
        return snapshot
