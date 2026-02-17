from fastapi import status
from fastapi.testclient import TestClient


def test_no_vary_header_when_htmx_not_added(
    client: TestClient,
) -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "Vary" not in response.headers


def test_vary_header_added_when_htmx_midddleware_added(
    htmx_enabled_client: TestClient,
) -> None:
    response = htmx_enabled_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "Vary" in response.headers
