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
            "Influencer": "Pendente de Definição",
            "Tipo Influencer": "Pendente de Definição",
            "Data de referência": "Pendente de Definição",
            "Rentabilidade Vai na Cola": "15%",
            "Desenquadrado": "05/06/2022"
        }
