from typing import Dict, List

from func.src.domain.validator import Portfolio, Wallet, VaiNaColaWalletReport


class VaiNaColaService:

    @classmethod
    def get_vai_na_cola_portfolio_report(cls, portfolio: Portfolio) -> List[VaiNaColaWalletReport]:
        portfolio_report = []
        br_portfolio_report = cls._request_vnc_br_portfolio_report(portfolio.wallets_vnc_br)
        portfolio_report += br_portfolio_report
        return portfolio_report

    @classmethod
    def _request_vnc_br_portfolio_report(cls, wallets_vnc_br: Dict[str, Wallet]) -> List[VaiNaColaWalletReport]:
        portfolio_report = [
            cls._request_vnc_br_wallet_report(wallet_id, wallet)
            for wallet_id, wallet in wallets_vnc_br.items()
        ]
        return portfolio_report

    @staticmethod
    def _request_vnc_br_wallet_report(wallet_id: str, wallet: Wallet) -> VaiNaColaWalletReport:
        return VaiNaColaWalletReport(
            id=wallet_id,
            influencer="Pendente de Definição",
            influencer_type="Pendente de Definição",
            report_date="Pendente de Definição",
            profitability="15%",
            rebalance_date="05/06/2022",
        )
