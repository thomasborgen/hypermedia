from unittest.mock import Mock

from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from hypermedia import Div
from tests.fastapi.index import render_index, render_index_partial


def test_full_html_returned(
    client: TestClient,
) -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "full" in response.text
    assert "partial" in response.text


def test_only_partial_html_returned(
    client: TestClient,
) -> None:
    response = client.get("/", headers={"HX-Request": "true"})
    assert response.status_code == status.HTTP_200_OK
    assert "full" not in response.text
    assert "partial" in response.text


def test_render_index_partial_called(
    app: FastAPI,
    client: TestClient,
) -> None:
    mock_partial = Mock(return_value=Div("mocked"))
    app.dependency_overrides[render_index_partial] = lambda: mock_partial()

    client.get("/", headers={"HX-Request": "true"})

    mock_partial.assert_called_once()


def test_render_index_not_called(
    app: FastAPI,
    client: TestClient,
) -> None:
    mock_full = Mock(return_value=Div("mocked"))
    app.dependency_overrides[render_index] = lambda: mock_full()

    client.get("/", headers={"HX-Request": "true"})

    mock_full.assert_not_called()


def test_render_index_partial_called_only_once_on_full(
    app: FastAPI,
    client: TestClient,
) -> None:
    mock_partial = Mock(return_value=Div("mocked"))
    app.dependency_overrides[render_index_partial] = lambda: mock_partial()

    client.get("/")

    mock_partial.assert_called_once()


def test_render_partial_data_only_when_no_full_available(
    client: TestClient,
) -> None:
    response = client.get("/partial")

    assert "full" not in response.text
    assert "partial" in response.text


def test_render_partial_data_only_when_no_full_available_htmx(
    client: TestClient,
) -> None:
    response = client.get("/partial", headers={"HX-Request": "true"})

    assert "full" not in response.text
    assert "partial" in response.text
