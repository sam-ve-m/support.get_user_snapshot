class VaiNaColaSnapshotRepository:
    @classmethod
    def snapshot(cls, user_data: dict) -> list:
        vai_na_cola = [
            cls._request_vnc_wallet_data(wallet.get("bovespa_account"))
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        ]
        return vai_na_cola

    @classmethod
    def _request_vnc_wallet_data(cls, bovespa_account: str) -> dict:
        return {
            "Carteira/Código": bovespa_account,
            "Influencer": None,
            "Tipo Influencer": None,
            "Data de referência": None,
            "Rentabilidade Vai na Cola": "15%",
            "Desenquadrado": "05/06/2022"
        }
