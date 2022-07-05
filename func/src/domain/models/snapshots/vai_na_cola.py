from typing import List

from func.src.domain.validator import VaiNaColaWalletReport


class VaiNaColaReport:
    def __init__(self, vnc_portfolio_report: List[VaiNaColaWalletReport]):
        self.__vnc_portfolio_report = vnc_portfolio_report

    @staticmethod
    def __normalize_vnc_wallet_report(wallet_report: VaiNaColaWalletReport) -> list:
        normalized_vnc_wallet_report = [
            {"value": wallet_report.id, "label": "Carteira/Código"},
            {"value": "Pendente de Definição", "label": "Influencer"},
            {"value": "Pendente de Definição", "label": "Tipo Influencer"},
            {"value": "Pendente de Definição", "label": "Data de referência"},
            {"value": "15%", "label": "Rentabilidade Vai na Cola"},
            {"value": "05/06/2022", "label": "Desenquadrado"},
        ]
        return normalized_vnc_wallet_report

    def __normalize_vnc_portfolio_report(self) -> list:
        normalized_vnc_portfolio_report = [
            self.__normalize_vnc_wallet_report(wallet_report)
            for wallet_report in self.__vnc_portfolio_report
        ]
        return normalized_vnc_portfolio_report

    def get_snapshot(self) -> list:
        snapshot = self.__normalize_vnc_portfolio_report()
        return snapshot
