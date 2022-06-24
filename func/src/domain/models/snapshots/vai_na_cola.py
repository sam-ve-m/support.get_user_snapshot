# TODO: Verificar viablidade de ser apenas uma instância da classe "Wallet <-> Porftolio"
class VaiNaCola:
    def __init__(self, user_data: dict):

        #TODO: Assim como Wallet deve tratar apenas uma caretira do vai na cola por instância, não deve colocar todas dentro do mesmo objeto
        #TODO: Para tal deve receber o número da conta no parâmetro

        self.__vai_na_cola = [
            self._request_vnc_wallet_data(wallet.get("bovespa_account"))
            for wallet in user_data.get('portfolios', {}).get('vnc', {}).get('br', [])
        ]

    # TODO: A request para os dados da carteira do vai na cola não deve ser realizada aqui dentro do model, deve receber os dados como parâmetro do init
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
        # TODO: Uma vez que a classe só trata um portolio por vez, deve-se fazer essa junção na camada de serviço com o retorno de cada "get_snapshot" por carteira
        snapshot = [self.__normalize_vnc_wallet_data(wallet) for wallet in self.__vai_na_cola]
        return snapshot
