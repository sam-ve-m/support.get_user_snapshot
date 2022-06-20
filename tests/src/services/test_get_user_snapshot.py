# Jormungandr
from unittest.mock import MagicMock

import pytest

from func.src.domain.validator import Onboarding, Snapshots
from func.src.services.get_user_snapshot import GetUserSnapshotService
from unittest.mock import patch


dummy_decoded_jwt = {"user": {"unique_id": "159951"}}
mocked_pid = MagicMock()
mocked_onboarding_repo = MagicMock()
mocked_wallet = MagicMock()
mocked_vai_na_cola = MagicMock()
mocked_blocked_assets = MagicMock()
mocked_user_blocks = MagicMock()
mocked_warranty_assets = MagicMock()
mocked_warranty = MagicMock()


@patch.object(Onboarding, "__init__", return_value=None)
@patch.object(Snapshots, "__init__", return_value=None)
def test_snapshot_user_data(mocked_onboarding, mocked_snapshot, monkeypatch):
    monkeypatch.setattr(
        GetUserSnapshotService,
        "user_repository",
        MagicMock(find_user_by_unique_id=MagicMock(return_value=True))
    )
    monkeypatch.setattr(GetUserSnapshotService, "pid_snapshot_repository", mocked_pid)
    monkeypatch.setattr(GetUserSnapshotService, "onboarding_snapshot_repository", mocked_onboarding_repo)
    monkeypatch.setattr(GetUserSnapshotService, "wallet_snapshot_repository", mocked_wallet)
    monkeypatch.setattr(GetUserSnapshotService, "vai_na_cola_snapshot_repository", mocked_vai_na_cola)
    monkeypatch.setattr(GetUserSnapshotService, "blocked_assets_snapshot_repository", mocked_blocked_assets)
    monkeypatch.setattr(GetUserSnapshotService, "user_blocks_snapshot_repository", mocked_user_blocks)
    monkeypatch.setattr(GetUserSnapshotService, "warranty_assets_snapshot_repository", mocked_warranty_assets)
    monkeypatch.setattr(GetUserSnapshotService, "warranty_snapshot_repository", mocked_warranty)
    GetUserSnapshotService.snapshot_user_data(dummy_decoded_jwt)
    mocked_onboarding.assert_called_once()
    mocked_snapshot.assert_called_once()
    mocked_pid.snapshot.assert_called_once()
    mocked_onboarding_repo.snapshot.assert_called_once()
    mocked_wallet.snapshot.assert_called_once()
    mocked_vai_na_cola.snapshot.assert_called_once()
    mocked_blocked_assets.snapshot.assert_called_once()
    mocked_user_blocks.snapshot.assert_called_once()
    mocked_warranty_assets.snapshot.assert_called_once()
    mocked_warranty.snapshot.assert_called_once()


def test_snapshot_user_data_no_user(monkeypatch):
    monkeypatch.setattr(
        GetUserSnapshotService,
        "user_repository",
        MagicMock(find_user_by_unique_id=MagicMock(return_value=False))
    )
    with pytest.raises(ValueError):
        GetUserSnapshotService.snapshot_user_data(dummy_decoded_jwt)
