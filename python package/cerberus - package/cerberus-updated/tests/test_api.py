import json
import os

import pytest

from src.Api import Api

API = Api()
KEY = "KEY"
VALUE = "VALUE"


@pytest.fixture
def test_payload():
    with open(os.path.abspath("resources/payload.json")) as f:
        return json.loads(f.read())


@pytest.mark.parametrize(
    "parameters",
    [
        {KEY: "id", VALUE: -1},
        {KEY: "id", VALUE: 101}
    ],
    ids=["too_small_id", "too_large_id"]
)
def test_invalid_payload(parameters, test_payload):
    test_payload[parameters[KEY]] = parameters[VALUE]

    with pytest.raises(SystemExit) as pytest_wrapped_exception:
        API.validate_payload(test_payload)

    assert pytest_wrapped_exception.type == SystemExit


def test_valid_payload(test_payload):
    API.validate_payload(test_payload)


def test_customer_instantiation(test_payload):
    customer = API.create_customer(test_payload)

    assert customer is not None

    assert customer.id == test_payload["id"]
    assert customer.name == test_payload["name"]
    assert customer.accounts == test_payload["accounts"]
    assert customer.contact_details == test_payload["contact_details"]
