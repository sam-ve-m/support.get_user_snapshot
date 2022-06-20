from typing import List


class WalletSnapshotRepository:
    @classmethod
    def snapshot(cls, user_data: dict) -> list:
        default_wallets_ids = cls._find_default_wallets_ids(user_data)
        vnc_wallets_ids = cls._find_vnc_wallets_ids(user_data)
        wallets_ids = {**default_wallets_ids, **vnc_wallets_ids}
        portfolio = []
        for wallet_id, wallet_name in wallets_ids.items():
            portfolio += cls._request_wallet_portfolio(wallet_name, wallet_id)
        return portfolio

    @classmethod
    def _find_default_wallets_ids(cls, user_data: dict) -> dict:
        default_wallet = user_data.get('portfolios', {}).get('default', {})
        wallets = {
            **cls._find_wallet_id_br(default_wallet),
            **cls._find_wallet_id_us(default_wallet),
        }
        return wallets

    @staticmethod
    def _find_wallet_id_br(default_wallet: dict) -> dict:
        if walled_id_br := default_wallet.get("br", {}).get("bovespa_account"):
            return {walled_id_br: "Brazuca"}
        return {}

    @staticmethod
    def _find_wallet_id_us(default_wallet: dict) -> dict:
        if walled_id_us := default_wallet.get("us", {}).get("dw_account"):
            return {walled_id_us: "Gringa"}
        return {}

    @classmethod
    def _find_vnc_wallets_ids(cls, user_data: dict) -> dict:
        wallets_ids = {
            wallet.get("bovespa_account"): "Vai na Cola"
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        }
        return wallets_ids

    @classmethod
    def _request_wallet_portfolio(cls, wallet_name: str, walled_id: str) -> List[dict]:
        ...  # TODO: Pegar os dados da carteira do cliente
        portfolio = [{
            "Código de bolsa": walled_id,
            "Nome da carteira": wallet_name,
            "Ativo": "PETR4",
            "Preço Médio": 15.45,
            "Quantidade": 400,
            "Quantidade inicial": 150,
            "Valor Gasto": 618,
            "Valor Atual": 16,
        }]*2
        return portfolio
