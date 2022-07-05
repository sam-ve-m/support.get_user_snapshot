from func.src.domain.validator import Wallet, Asset


class BlockedAssets:
    def __init__(self, blocked_wallet: Wallet):
        self.__blocked_assets = blocked_wallet

    @staticmethod
    def __normalize_assets(asset: Asset) -> list:
        normalized_asset = [
            {"value": asset.ticker, "label": "Ativo"},
            {"value": asset.current_value, "label": "Valor"},
            {"value": asset.current_quantity, "label": "Quantidade"},
        ]
        return normalized_asset

    def get_snapshot(self) -> list:
        snapshot = [self.__normalize_assets(asset) for asset in self.__blocked_assets]
        return snapshot
