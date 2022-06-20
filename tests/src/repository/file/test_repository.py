from unittest.mock import MagicMock, AsyncMock, patch

import pytest

from func.src.repository.file.repository import FileRepository
from tests.test_utils.utils import create_fake_async_context_yielding_value, create_async_iterable_object


fake_bucket = MagicMock()
fake_resource = AsyncMock()
fake_resource.Bucket.return_value = fake_bucket
fake_infra = AsyncMock(get_resource=create_fake_async_context_yielding_value(fake_resource))

dummy_unique_id = "159159"
dummy_bucket_name = "Bucket"
dummy_file_type = "selfie"
stub_file_type = MagicMock(value=dummy_file_type)
dummy_path = "159159/selfie/"


@pytest.mark.asyncio
@patch.object(FileRepository, "_resolve_user_path", return_value=dummy_path)
async def test_user_file_exists(mocked_file_checker, monkeypatch):
    monkeypatch.setattr(FileRepository, "infra", fake_infra)
    fake_bucket.objects.filter.return_value = create_async_iterable_object([None] * 2)
    response = await FileRepository.user_file_exists(stub_file_type, dummy_unique_id, dummy_bucket_name)
    assert response is True


@pytest.mark.asyncio
@patch.object(FileRepository, "_resolve_user_path", return_value=dummy_path)
async def test_user_file_exists_no_objects(mocked_file_checker, monkeypatch):
    monkeypatch.setattr(FileRepository, "infra", fake_infra)
    fake_bucket.objects.filter.return_value = create_async_iterable_object([])
    response = await FileRepository.user_file_exists(stub_file_type, dummy_unique_id, dummy_bucket_name)
    assert response is False


def test_resolve_user_path():
    response = FileRepository._resolve_user_path(dummy_unique_id, stub_file_type)
    assert response == dummy_path
