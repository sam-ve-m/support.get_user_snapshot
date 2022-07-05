# # Jormungandr
# from unittest.mock import MagicMock
#
# import pytest
#
# from func.src.repository.user.repository import UserRepository
# from unittest.mock import patch
#
# from func.src.services.snapshot_builder.service import SnapshotBuilderService
#
# dummy_decoded_jwt = {"user": {"unique_id": "159951"}}
# dummy_user = {"some": "value"}
# mocked_pid = MagicMock()
# mocked_onboarding_repo = MagicMock()
# mocked_wallet = MagicMock()
# mocked_vai_na_cola = MagicMock()
# mocked_blocked_assets = MagicMock()
# mocked_user_blocks = MagicMock()
# mocked_warranty_assets = MagicMock()
# mocked_warranty = MagicMock()
#
#
# def test_snapshot_user_data(monkeypatch):
#     monkeypatch.setattr(
#         SnapshotBuilderService,
#         "user_repository",
#         MagicMock(find_user_by_unique_id=MagicMock(return_value=dummy_user))
#     )
#     monkeypatch.setattr(SnapshotBuilderService, "pid_model", mocked_pid)
#     monkeypatch.setattr(SnapshotBuilderService, "onboarding_model", mocked_onboarding_repo)
#     monkeypatch.setattr(SnapshotBuilderService, "wallet_model", mocked_wallet)
#     monkeypatch.setattr(SnapshotBuilderService, "vai_na_cola_model", mocked_vai_na_cola)
#     monkeypatch.setattr(SnapshotBuilderService, "blocked_assets_model", mocked_blocked_assets)
#     monkeypatch.setattr(SnapshotBuilderService, "user_blocks_model", mocked_user_blocks)
#     monkeypatch.setattr(SnapshotBuilderService, "warranty_assets_model", mocked_warranty_assets)
#     monkeypatch.setattr(SnapshotBuilderService, "warranty_model", mocked_warranty)
#     SnapshotBuilderService.snapshot_user_data(dummy_decoded_jwt)
#     mocked_pid.assert_called_once_with(dummy_user)
#     mocked_pid.return_value.get_snapshot.assert_called_once_with()
#     mocked_onboarding_repo.assert_called_once_with(dummy_user)
#     mocked_onboarding_repo.return_value.get_snapshot.assert_called_once_with()
#     mocked_wallet.assert_called_once_with(dummy_user)
#     mocked_wallet.return_value.get_snapshot.assert_called_once_with()
#     mocked_vai_na_cola.assert_called_once_with(dummy_user)
#     mocked_vai_na_cola.return_value.get_snapshot.assert_called_once_with()
#     mocked_blocked_assets.assert_called_once_with(dummy_user)
#     mocked_blocked_assets.return_value.get_snapshot.assert_called_once_with()
#     mocked_user_blocks.assert_called_once_with(dummy_user)
#     mocked_user_blocks.return_value.get_snapshot.assert_called_once_with()
#     mocked_warranty_assets.assert_called_once_with(dummy_user)
#     mocked_warranty_assets.return_value.get_snapshot.assert_called_once_with()
#     mocked_warranty.assert_called_once_with(dummy_user)
#     mocked_warranty.return_value.get_snapshot.assert_called_once_with()
#
#
# @patch.object(UserRepository, "find_user_by_unique_id", return_value=False)
# def test_snapshot_user_data_no_user(monkeypatch):
#     with pytest.raises(ValueError):
#         SnapshotBuilderService.snapshot_user_data(dummy_decoded_jwt)
