from fastapi.testclient import TestClient


def test_no_vary_header_when_htmx_not_added(
    client: TestClient,
) -> None:
    response = client.get("/hypermedia")
    assert "partial" in response.text
    assert "full" in response.text


def test_get_path():
    