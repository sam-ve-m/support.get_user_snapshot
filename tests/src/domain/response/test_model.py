# Jormungandr
from func.src.domain.enums import CodeResponse
from func.src.domain.validator import Snapshots
from func.src.domain.response.model import ResponseModel

# Standards
import json

# Third party
from flask import Response
from nidavellir import Sindri
from unittest.mock import MagicMock, patch


dummy_snapshots = {}
stub_snapshots = MagicMock()
stub_snapshots.dict.return_value = dummy_snapshots

dummy_response_code = 200
stub_response_code = MagicMock(value=dummy_response_code)

fake_dumps = MagicMock(return_value=True)


@patch.object(json, "dumps", return_value=True)
@patch.object(Sindri, "resolver")
def test_build_response(mocked_resolver, mocked_dumps):
    response = ResponseModel.build_response(stub_snapshots, stub_response_code)
    mocked_dumps.assert_called_once_with(
        {"result": dummy_snapshots, "code": dummy_response_code},
        default=mocked_resolver
    )
    assert response is True


dummy_error_message = "erro"


@patch.object(json, "dumps", return_value=True)
@patch.object(Sindri, "resolver")
def test_build_error_response(mocked_resolver, mocked_dumps):
    response = ResponseModel.build_error_response(dummy_error_message, stub_response_code)
    mocked_dumps.assert_called_once_with(
        {"message": dummy_error_message, "code": dummy_response_code},
        default=mocked_resolver
    )
    assert response is True


dummy_response_model = "response_model"
dummy_mimetype = "mimetype"


@patch.object(Response, "__init__", return_value=None)
def test_build_http_response(mocked_response_model):
    ResponseModel.build_http_response(dummy_response_model, stub_response_code, dummy_mimetype)
    mocked_response_model.assert_called_once_with(
        dummy_response_model,
        mimetype=dummy_mimetype,
        status=dummy_response_code,
    )
