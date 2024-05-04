from apis.inference.online.api import OnlineInference
from fastapi.testclient import TestClient
from datetime import datetime
import pytest


@pytest.fixture(scope="module")
def test_client() -> TestClient:
    api = OnlineInference.instantiate_api()
    return TestClient(api.app)


@pytest.fixture(scope="module")
def healthcheck_response(test_client: TestClient):
    response = test_client.get("/health_check")
    return response


def test_health_check_success(healthcheck_response):
    assert healthcheck_response.status_code == 200


def test_health_check_body(healthcheck_response):
    resp_body = healthcheck_response.json()
    assert resp_body["name"] == "OnlineInference"
    assert resp_body["version"] == OnlineInference.__version__
    assert resp_body["status_message"] == "No data sources configured."
    assert resp_body["status"] == healthcheck_response.status_code
    assert resp_body["timezone"] == str(datetime.now().astimezone().tzinfo)
