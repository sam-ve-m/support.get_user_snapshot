# Jormungandr
from unittest.mock import MagicMock

import pytest

from func.src.domain.validator import Snapshots
from func.src.services.get_user_snapshot import GetUserSnapshotService
from unittest.mock import patch


dummy_decoded_jwt = {"user": {"unique_id": "159951"}}
dummy_user = {"some": "value"}
mocked_pid = MagicMock()
mocked_onboarding_repo = MagicMock()
mocked_wallet = MagicMock()
mocked_vai_na_cola = MagicMock()
mocked_blocked_assets = MagicMock()
mocked_user_blocks = MagicMock()
mocked_warranty_assets = MagicMock()
mocked_warranty = MagicMock()


@patch.object(Snapshots, "__init__", return_value=None)
def test_snapshot_user_data(mocked_snapshot, monkeypatch):
    monkeypatch.setattr(
        GetUserSnapshotService,
        "user_repository",
        MagicMock(find_user_by_unique_id=MagicMock(return_value=dummy_user))
    )
    monkeypatch.setattr(GetUserSnapshotService, "pid_model", mocked_pid)
    monkeypatch.setattr(GetUserSnapshotService, "onboarding_model", mocked_onboarding_repo)
    monkeypatch.setattr(GetUserSnapshotService, "wallet_model", mocked_wallet)
    monkeypatch.setattr(GetUserSnapshotService, "vai_na_cola_model", mocked_vai_na_cola)
    monkeypatch.setattr(GetUserSnapshotService, "blocked_assets_model", mocked_blocked_assets)
    monkeypatch.setattr(GetUserSnapshotService, "user_blocks_model", mocked_user_blocks)
    monkeypatch.setattr(GetUserSnapshotService, "warranty_assets_model", mocked_warranty_assets)
    monkeypatch.setattr(GetUserSnapshotService, "warranty_model", mocked_warranty)
    GetUserSnapshotService.snapshot_user_data(dummy_decoded_jwt)
    mocked_snapshot.assert_called_once()
    mocked_pid.assert_called_once_with(dummy_user)
    mocked_pid.return_value.get_snapshot.assert_called_once_with()
    mocked_onboarding_repo.assert_called_once_with(dummy_user)
    mocked_onboarding_repo.return_value.get_snapshot.assert_called_once_with()
    mocked_wallet.assert_called_once_with(dummy_user)
    mocked_wallet.return_value.get_snapshot.assert_called_once_with()
    mocked_vai_na_cola.assert_called_once_with(dummy_user)
    mocked_vai_na_cola.return_value.get_snapshot.assert_called_once_with()
    mocked_blocked_assets.assert_called_once_with(dummy_user)
    mocked_blocked_assets.return_value.get_snapshot.assert_called_once_with()
    mocked_user_blocks.assert_called_once_with(dummy_user)
    mocked_user_blocks.return_value.get_snapshot.assert_called_once_with()
    mocked_warranty_assets.assert_called_once_with(dummy_user)
    mocked_warranty_assets.return_value.get_snapshot.assert_called_once_with()
    mocked_warranty.assert_called_once_with(dummy_user)
    mocked_warranty.return_value.get_snapshot.assert_called_once_with()


def test_snapshot_user_data_no_user(monkeypatch):
    monkeypatch.setattr(
        GetUserSnapshotService,
        "user_repository",
        MagicMock(find_user_by_unique_id=MagicMock(return_value=False))
    )
    with pytest.raises(ValueError):
        GetUserSnapshotService.snapshot_user_data(dummy_decoded_jwt)
