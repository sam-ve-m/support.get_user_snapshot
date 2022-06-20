from unittest.mock import patch, AsyncMock
import aioboto3
from decouple import AutoConfig
import pytest
from etria_logger import Gladsheim

from func.src.infrastructure.bucket.infrastructure import BucketInfrastructure
from tests.test_utils.utils import create_fake_async_context_yielding_value

dummy_session = "dummy session"


@patch.object(AutoConfig, "__call__")
@patch.object(aioboto3, "Session", return_value=dummy_session)
def test_get_session(mock_s3_session, mocked_env):
    new_session_created = BucketInfrastructure._get_session()
    assert new_session_created == dummy_session
    mock_s3_session.assert_called_once()

    reused_client = BucketInfrastructure._get_session()
    assert reused_client == new_session_created
    mock_s3_session.assert_called_once()


dummy_resource = "dummy resource"
fake_session = AsyncMock(resource=create_fake_async_context_yielding_value(dummy_resource))


@pytest.mark.asyncio
@patch.object(BucketInfrastructure, "_get_session", return_value=fake_session)
async def test_get_resource(mocked_get_session):
    async with BucketInfrastructure.get_resource() as resource:
        assert resource == dummy_resource


stub_error = AssertionError()


@pytest.mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(BucketInfrastructure, "_get_session", side_effect=stub_error)
async def test_get_resource_with_errors(mocked_get_session, mocked_logger):
    with pytest.raises(stub_error.__class__):
        async with BucketInfrastructure.get_resource():
            raise ValueError("This line is not supposed to be reached. If so, the test failed.")
    mocked_logger.assert_called_once()
