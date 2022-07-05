from func.src.domain.validator import Wallet, Portfolio, Asset


class PortfolioService:
    @classmethod
    def request_user_portfolio(cls, user_data) -> Portfolio:
        br_wallet_id = cls._find_wallet_id_br(user_data)
        br_wallet = cls._request_wallet_br(br_wallet_id)
        us_wallet_id = cls._find_wallet_id_us(user_data)
        us_wallet = cls._request_wallet_us(us_wallet_id)
        vnc_br_wallets_ids = cls._find_wallets_ids_vnc_br(user_data)
        vnc_br_wallets = {wallet_id: cls._request_wallet_vai_na_cola_br(wallet_id) for wallet_id in vnc_br_wallets_ids}
        return Portfolio(
            wallet_id_br=br_wallet_id,
            wallet_br=br_wallet,
            wallet_id_us=us_wallet_id,
            wallet_us=us_wallet,
            wallets_vnc_br=vnc_br_wallets,
        )

    @staticmethod
    def _find_wallet_id_br(user_data) -> str:
        wallet_id = user_data.get('portfolios', {}).get('default', {}).get("br", {}).get("bovespa_account")
        return wallet_id

    @staticmethod
    def _find_wallet_id_us(user_data) -> str:
        wallet_id = user_data.get('portfolios', {}).get('default', {}).get("us", {}).get("dw_account")
        return wallet_id

    @staticmethod
    def _find_wallets_ids_vnc_br(user_data) -> tuple:
        wallets_ids = tuple(
            wallet.get("bovespa_account")
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        )
        return wallets_ids

    @staticmethod
    def _request_wallet_br(wallet_id: str) -> Wallet:
        wallet_br = [Asset(
            ticker="PETR4",
            mean_price=15.45,
            initial_quantity=10,
            current_quantity=50,
            spent_value=154.50,
            current_value=800.45,
        )]*2
        return wallet_br

    @staticmethod
    def _request_wallet_us(wallet_id: str) -> Wallet:
        wallet_us = [Asset(
            ticker="AAPL",
            mean_price=34.56,
            initial_quantity=10,
            current_quantity=60,
            spent_value=345.60,
            current_value=2451.23,
        )]*2
        return wallet_us

    @staticmethod
    def _request_wallet_vai_na_cola_br(wallet_id: str) -> Wallet:
        wallet_vnc_br = [Asset(
            ticker="JBSS3",
            mean_price=45.15,
            initial_quantity=10,
            current_quantity=50,
            spent_value=451.50,
            current_value=6584.72,
        )]*2
        return wallet_vnc_br
