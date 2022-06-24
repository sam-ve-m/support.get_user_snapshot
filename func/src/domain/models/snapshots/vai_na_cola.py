class VaiNaCola:
    def __init__(self, user_data: dict):
        self.__vai_na_cola = [
            self._request_vnc_wallet_data(wallet.get("bovespa_account"))
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        ]

    def _request_vnc_wallet_data(cls, bovespa_account: str) -> dict:
        vnc_wallet_data = {"_id": bovespa_account}
        return vnc_wallet_data

    @staticmethod
    def __normalize_vnc_wallet_data(wallet_data: dict) -> list:
        normalized_vnc_wallet_data = [
            {"value": wallet_data.get("_id"), "label": "Carteira/Código"},
            {"value": "Pendente de Definição", "label": "Influencer"},
            {"value": "Pendente de Definição", "label": "Tipo Influencer"},
            {"value": "Pendente de Definição", "label": "Data de referência"},
            {"value": "15%", "label": "Rentabilidade Vai na Cola"},
            {"value": "05/06/2022", "label": "Desenquadrado"},
        ]
        return normalized_vnc_wallet_data

    def get_snapshot(self) -> list:
        snapshot = [self.__normalize_vnc_wallet_data(wallet) for wallet in self.__vai_na_cola]
        return snapshot
