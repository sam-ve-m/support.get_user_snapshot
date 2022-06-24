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

    @staticmethod
    def snapshot_user_data(decoded_jwt: dict) -> Snapshots:
        unique_id = decoded_jwt.get("user").get("unique_id")
        if not (user_data := UserRepository.find_user_by_unique_id(unique_id=unique_id)):
            raise ValueError("Unable to find user")  # TODO: melhorar excessão

        snapshots = Snapshots(
            pid=PID(user_data).get_snapshot(),
            onboarding=Onboarding(user_data).get_snapshot(),
            wallet=Wallet(user_data).get_snapshot(),
            vai_na_cola=VaiNaCola(user_data).get_snapshot(),
            blocked_assets=BlockedAssets(user_data).get_snapshot(),
            user_blocks=UserBlocks(user_data).get_snapshot(),
            warranty_assets=WarrantyAssets(user_data).get_snapshot(),
            warranty=Warranty(user_data).get_snapshot(),
        )
        return snapshots
