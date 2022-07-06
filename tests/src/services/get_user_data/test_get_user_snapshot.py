from unittest.mock import patch

import pytest

from func.src.repository.user.repository import UserRepository
from func.src.services.get_user_data.service import GetUserDataService

dummy_user_data_empty = None
dummy_unique_id = "Unique Id"
dummy_user_data = {"some": "value"}
stub_jwt = {"user": {"unique_id": dummy_unique_id}}


@patch.object(UserRepository, "find_user_by_unique_id", return_value=dummy_user_data)
def test_get_user_data(mocked_find_user):
    response = GetUserDataService.get_user_data(stub_jwt)
    mocked_find_user.assert_called_once_with(unique_id=dummy_unique_id)
    assert response == dummy_user_data


@patch.object(UserRepository, "find_user_by_unique_id", return_value=dummy_user_data_empty)
def test_get_user_data_empty(mocked_find_user):
    with pytest.raises(ValueError):
        GetUserDataService.get_user_data(stub_jwt)
    mocked_find_user.assert_called_once_with(unique_id=dummy_unique_id)
