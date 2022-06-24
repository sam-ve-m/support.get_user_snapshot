# Jormungandr

from ..domain.validator import Snapshots
from func.src.domain.models.snapshots.blocked_assets import BlockedAssets
from func.src.domain.models.snapshots.onboarding import Onboarding
from func.src.domain.models.snapshots.pid import PID
from func.src.domain.models.snapshots.user_blocks import UserBlocks
from func.src.domain.models.snapshots.vai_na_cola import VaiNaCola
from func.src.domain.models.snapshots.wallet import Wallet
from func.src.domain.models.snapshots.warranty_assets import WarrantyAssets
from func.src.domain.models.snapshots.warranty import Warranty
from ..repository.user.repository import UserRepository


class GetUserSnapshotService:
    user_repository = UserRepository
    pid_model = PID
    onboarding_model = Onboarding
    wallet_model = Wallet
    vai_na_cola_model = VaiNaCola
    blocked_assets_model = BlockedAssets
    user_blocks_model = UserBlocks
    warranty_assets_model = WarrantyAssets
    warranty_model = Warranty

    @classmethod
    def snapshot_user_data(cls, decoded_jwt: dict) -> Snapshots:
        unique_id = decoded_jwt.get("user").get("unique_id")
        if not (user_data := cls.user_repository.find_user_by_unique_id(unique_id=unique_id)):
            raise ValueError("Unable to find user")  # TODO: melhorar excessão
        snapshots = Snapshots(
            pid=cls.pid_model(user_data).get_snapshot(),
            onboarding=cls.onboarding_model(user_data).get_snapshot(),
            wallet=cls.wallet_model(user_data).get_snapshot(),
            vai_na_cola=cls.vai_na_cola_model(user_data).get_snapshot(),
            blocked_assets=cls.blocked_assets_model(user_data).get_snapshot(),
            user_blocks=cls.user_blocks_model(user_data).get_snapshot(),
            warranty_assets=cls.warranty_assets_model(user_data).get_snapshot(),
            warranty=cls.warranty_model(user_data).get_snapshot(),
        )
        return snapshots
