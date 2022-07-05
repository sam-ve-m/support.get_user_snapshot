from func.src.domain.validator import Wallet, Asset


class WarrantyAssets:
    def __init__(self, warranty_wallet: Wallet):
        self.__warranty_assets = warranty_wallet

    @staticmethod
    def __normalize_assets(asset: Asset) -> list:
        normalized_asset = [
            {"value": asset.ticker, "label": "Ativo"},
            {"value": asset.current_value, "label": "Valor"},
            {"value": asset.current_quantity, "label": "Quantidade"},
        ]
        return normalized_asset

    def get_snapshot(self) -> list:
        snapshot = [self.__normalize_assets(asset) for asset in self.__warranty_assets]
        return snapshot
