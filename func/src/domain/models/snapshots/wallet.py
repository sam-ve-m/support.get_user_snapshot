from func.src.domain.validator import Asset, Wallet


class BaseWallet:
    wallet_name: str

    def __init__(self, wallet_id: str, wallet: Wallet):
        self.__wallet_assets = wallet
        self.__wallet_id = wallet_id

    def __normalize_asset(self, asset: Asset) -> list:
        normalized_asset = [
            {"label": "Código de bolsa", "value": self.__wallet_id},
            {"label": "Nome da carteira", "value": self.wallet_name},
            {"label": "Ativo", "value": asset.ticker},
            {"label": "Preço Médio", "value": asset.mean_price},
            {"label": "Quantidade", "value": asset.current_quantity},
            {"label": "Quantidade inicial", "value": asset.initial_quantity},
            {"label": "Valor Gasto", "value": asset.spent_value},
            {"label": "Valor Atual", "value": asset.current_value}
        ]
        return normalized_asset

    def __normalize_wallet(self) -> list:
        normalized_wallet = [self.__normalize_asset(asset) for asset in self.__wallet_assets]
        return normalized_wallet

    def get_snapshot(self) -> list:
        snapshot = self.__normalize_wallet()
        return snapshot


class WalletBR(BaseWallet):
    wallet_name: str = "Brazuca"


class WalletUS(BaseWallet):
    wallet_name: str = "Gringa"


class WalletVaiNaColaBR(BaseWallet):
    wallet_name: str = "Vai na Cola BR"
