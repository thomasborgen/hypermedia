from fastapi import status
from fastapi.testclient import TestClient


def test_get_non_instrumented(
    client: TestClient,
) -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "Vary" not in response.headers


def test_vary_header_added_when_instrumented(
    instrumented_client: TestClient,
) -> None:
    response = instrumented_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "Vary" in response.headers
