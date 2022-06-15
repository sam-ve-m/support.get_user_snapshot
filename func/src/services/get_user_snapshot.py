# Jormungandr

from ..domain.validator import Onboarding, Snapshots
from ..repository.snapshots.blocked_assets import BlockedAssetsSnapshotRepository
from ..repository.snapshots.onboarding import OnboardingSnapshotRepository
from ..repository.snapshots.pid import PIDSnapshotRepository
from ..repository.snapshots.user_blocks import UserBlocksSnapshotRepository
from ..repository.snapshots.vai_na_cola import VaiNaColaSnapshotRepository
from ..repository.snapshots.wallet import WalletSnapshotRepository
from ..repository.snapshots.warranty import WarrantyAssetsSnapshotRepository
from ..repository.snapshots.warranty_assets import WarrantySnapshotRepository
from ..repository.user.repository import UserRepository


class GetUserSnapshotService:
    user_repository = UserRepository
    pid_snapshot_repository = PIDSnapshotRepository
    onboarding_snapshot_repository = OnboardingSnapshotRepository
    wallet_snapshot_repository = WalletSnapshotRepository
    vai_na_cola_snapshot_repository = VaiNaColaSnapshotRepository
    blocked_assets_snapshot_repository = BlockedAssetsSnapshotRepository
    user_blocks_snapshot_repository = UserBlocksSnapshotRepository
    warranty_assets_snapshot_repository = WarrantyAssetsSnapshotRepository
    warranty_snapshot_repository = WarrantySnapshotRepository

    @classmethod
    def snapshot_user_data(cls, decoded_jwt: dict):
        unique_id = decoded_jwt.get("user").get("unique_id")
        if not (user_data := cls.user_repository.find_user_by_unique_id(unique_id=unique_id)):
            raise ValueError("Unable to find user")  # TODO: melhorar excessão
        onboarding_status = Onboarding(user_data=user_data)
        snapshots = Snapshots(
            pid=cls.pid_snapshot_repository.snapshot(user_data),
            onboarding=cls.onboarding_snapshot_repository.snapshot(onboarding_status),
            wallet=cls.wallet_snapshot_repository.snapshot(user_data),
            vai_na_cola=cls.vai_na_cola_snapshot_repository.snapshot(user_data),
            blocked_assets=cls.blocked_assets_snapshot_repository.snapshot(user_data),
            user_blocks=cls.user_blocks_snapshot_repository.snapshot(user_data),
            warranty_assets=cls.warranty_assets_snapshot_repository.snapshot(user_data),
            warranty=cls.warranty_snapshot_repository.snapshot(user_data),
        )
        return snapshots
