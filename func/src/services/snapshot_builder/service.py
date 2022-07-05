# Jormungandr
from typing import List

from func.src.domain.models.snapshots.blocked_assets import BlockedAssets
from func.src.domain.models.snapshots.onboarding import Onboarding
from func.src.domain.models.snapshots.pid import PID
from func.src.domain.models.snapshots.user_blocks import UserBlocks
from func.src.domain.models.snapshots.vai_na_cola import VaiNaColaReport
from func.src.domain.models.snapshots.wallet import WalletBR, WalletUS, WalletVaiNaColaBR
from func.src.domain.models.snapshots.warranty import Warranty
from func.src.domain.models.snapshots.warranty_assets import WarrantyAssets
from func.src.domain.validator import Portfolio, VaiNaColaWalletReport, BlockSummary, Wallet, WarrantySummary


class SnapshotBuilderService:

    def __init__(self):
        self.__snapshot = {}

    def set_pid(self, user_data: dict):
        pid = PID(user_data).get_snapshot()
        self.__snapshot.update({"pid": pid})
        return self

    def set_onboarding(self, missed_steps_br: str, missed_steps_us: str):
        onboarding = Onboarding(
            missed_steps_br=missed_steps_br,
            date_of_missed_steps_br="??/??/????",
            missed_steps_us=missed_steps_us,
            date_of_missed_steps_us="??/??/????",
        ).get_snapshot()
        self.__snapshot.update({"onboarding": onboarding})
        return self

    def set_wallet(self, portfolio: Portfolio):
        wallet_br = WalletBR(portfolio.wallet_id_br, portfolio.wallet_br).get_snapshot()
        wallet_us = WalletUS(portfolio.wallet_id_us, portfolio.wallet_us).get_snapshot()
        wallets_vnc_br = (
            WalletVaiNaColaBR(wallet_id, wallet).get_snapshot()
            for wallet_id, wallet in portfolio.wallets_vnc_br.items()
        )

        wallet_snapshot = wallet_br + wallet_us
        for wallet in wallets_vnc_br:
            wallet_snapshot += wallet

        self.__snapshot.update({"wallet": wallet_snapshot})
        return self

    def set_vai_na_cola(self, vnc_portfolio_report: List[VaiNaColaWalletReport]):
        vai_na_cola = VaiNaColaReport(vnc_portfolio_report).get_snapshot()
        self.__snapshot.update({"vai_na_cola": vai_na_cola})
        return self

    def set_blocked_assets(self, blocked_assets: Wallet):
        blocked_assets = BlockedAssets(blocked_assets).get_snapshot()
        self.__snapshot.update({"blocked_assets": blocked_assets})
        return self

    def set_user_blocks(self, block_summary: BlockSummary):
        user_blocks = UserBlocks(block_summary).get_snapshot()
        self.__snapshot.update({"user_blocks": user_blocks})
        return self

    def set_warranty_assets(self, warranty_assets: Wallet):
        warranty_assets = WarrantyAssets(warranty_assets).get_snapshot()
        self.__snapshot.update({"warranty_assets": warranty_assets})
        return self

    def set_warranty(self, warranty_summary: WarrantySummary):
        warranty = Warranty(warranty_summary).get_snapshot()
        self.__snapshot.update({"warranty": warranty})
        return self

    def get_snapshot(self) -> dict:
        return self.__snapshot
