from typing import List


class WalletSnapshotRepository:
    @classmethod
    def snapshot(cls, user_data: dict) -> list:
        wallets = {
            **cls._find_default_wallets_ids(user_data),
            **{"Vai na Cola": wallet.get("bovespa_account")
                for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])}
        }
        portfolio = []
        for wallet_name, wallet_id in wallets.items():
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
            return {"Brazuca": walled_id_br}
        return {}

    @staticmethod
    def _find_wallet_id_us(default_wallet: dict) -> dict:
        if walled_id_us := default_wallet.get("us", {}).get("dw_account"):
            return {"Gringa": walled_id_us}
        return {}

    @classmethod
    def _request_wallet_portfolio(cls, wallet_name: str, walled_id: str) -> List[dict]:
        ...  # TODO: Pegar os dados da carteira do cliente
        portfolio = [{
            "Código de bolsa": walled_id,
            "Nome da carteira": wallet_name,
            "Ativo": f"PETR4",
            "Preço Médio": 15.45,
            "Quantidade": 400,
            "Quantidade inicial": 150,
            "Valor Gasto": 618,
            "Valor Atual": 16,
        }]*2
        return portfolio
