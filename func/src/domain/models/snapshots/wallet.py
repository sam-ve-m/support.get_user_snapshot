# TODO: Trocar o nome da classe para Portfolio
class Wallet:
    def __init__(self, user_data: dict):
        # TODO: Essa classe deve receber o portfolio a qual vai montar as posições, cada classe "Wallet" deve tratar unica e exclusivamente uma "Wallet"
        default_wallet = user_data.get('portfolios', {}).get('default', {})
        self.__wallet_id_br = default_wallet.get("br", {}).get("bovespa_account")
        self.__wallet_id_us = default_wallet.get("us", {}).get("dw_account")
        self.__portfolio_br = self._request_portfolio_br(self.__wallet_id_br)
        self.__portfolio_us = self._request_portfolio_us(self.__wallet_id_us)

        vnc_br_wallets_ids = (
            wallet.get("bovespa_account")
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        )
        self.__portfolio_vnc_br = {
            wallet_id: self._request_portfolio_vai_na_cola_br(wallet_id)
            for wallet_id in vnc_br_wallets_ids
        }

    # TODO: Essa request não deve ser feita dentro do objeto de domínio, deve receber estes dados como parâmetro do __init__
    def _request_portfolio_br(self, wallet_id: str) -> list:
        return [{}, {}]

    # TODO: Essa request não deve ser feita dentro do objeto de domínio, deve receber estes dados como parâmetro do __init__
    def _request_portfolio_us(self, wallet_id: str) -> list:
        return [{}, {}]

    # TODO: Essa request não deve ser feita dentro do objeto de domínio, deve receber estes dados como parâmetro do __init__
    def _request_portfolio_vai_na_cola_br(self, wallet_id: str) -> list:
        return [{}, {}]

    def __normalize_portfolio_br(self) -> list:
        normalized_portfolio_br = [[
            {"value": self.__wallet_id_br, "label": "Código de bolsa"},
            {"value": "Brazuca", "label": "Nome da carteira"},
            {"value": "PETR4", "label": "Ativo"},
            {"value": 15.45, "label": "Preço Médio"},
            {"value": 400, "label": "Quantidade"},
            {"value": 150, "label": "Quantidade inicial"},
            {"value": 618, "label": "Valor Gasto"},
            {"value": 16, "label": "Valor Atual"},
        ] for asset in self.__portfolio_br]
        return normalized_portfolio_br

    def __normalize_portfolio_us(self) -> list:
        normalized_portfolio_us = [[
            {"value": self.__wallet_id_us, "label": "Código de bolsa"},
            {"value": "Gringa", "label": "Nome da carteira"},
            {"value": "AAPL", "label": "Ativo"},
            {"value": 47.13, "label": "Preço Médio"},
            {"value": 26, "label": "Quantidade"},
            {"value": 2, "label": "Quantidade inicial"},
            {"value": 1000, "label": "Valor Gasto"},
            {"value": 48.54, "label": "Valor Atual"},
        ] for asset in self.__portfolio_us]
        return normalized_portfolio_us

    def __normalize_portfolio_vai_na_cola_br(self) -> list:
        normalized_portfolio_vai_na_cola_br = []
        for wallet_id, wallet in self.__portfolio_vnc_br.items():
            normalized_portfolio_vai_na_cola_br.extend([[
                {"value": wallet_id, "label": "Código de bolsa"},
                {"value": "Vai na Cola BR", "label": "Nome da carteira"},
                {"value": "VALE3", "label": "Ativo"},
                {"value": 32.55, "label": "Preço Médio"},
                {"value": 98, "label": "Quantidade"},
                {"value": 13, "label": "Quantidade inicial"},
                {"value": 400, "label": "Valor Gasto"},
                {"value": 30.41, "label": "Valor Atual"},
            ] for asset in wallet])
        return normalized_portfolio_vai_na_cola_br

    def get_snapshot(self) -> list:
        # TODO: Uma vez que a classe só trata um portolio por vez, deve-se fazer essa junção na camada de serviço com o retorno de cada "get_snapshot" por carteira
        snapshot = [
            *self.__normalize_portfolio_br(),
            *self.__normalize_portfolio_us(),
            *self.__normalize_portfolio_vai_na_cola_br(),
        ]
        return snapshot

