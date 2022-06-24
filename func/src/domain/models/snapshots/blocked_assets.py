class BlockedAssets:
    def __init__(self, user_data: dict):
        self.__blocked_assets = self._request_blocked_assets(user_data)

    # TODO: A request para os dados da carteira do vai na cola não deve ser realizada aqui dentro do model
    # TODO: Esse dado deve vir como parâmetro da classe BlockedAssets
    def _request_blocked_assets(self, user_data: dict) -> list:
        blocked_assets = [{}] * 3
        return blocked_assets

    @staticmethod
    def __normalize_assets(asset: dict) -> list:
        normalized_asset = [
            {"value": "Pendente de Definição", "label": "Ativo"},
            {"value": "Pendente de Definição", "label": "Preço Médio"},
            {"value": "Pendente de Definição", "label": "Quantidade"},
        ]
        return normalized_asset

    def get_snapshot(self) -> list:
        snapshot = [self.__normalize_assets(asset) for asset in self.__blocked_assets]
        return snapshot
