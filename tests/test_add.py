"""
Contract tests for POST /add against a running instance at http://0.0.0.0:5000.

Start the service before running:
    simpleadder   (or: uvicorn simpleadder.main:app --host 0.0.0.0 --port 5000)

Run tests:
    pytest tests/test_add.py -v
"""
from __future__ import annotations

import pytest
import httpx

BASE_URL = "http://0.0.0.0:5000"


@pytest.fixture(scope="session")
def client():
    """Shared HTTP client for the whole test session."""
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as c:
        yield c


# ---------------------------------------------------------------------------
# HTTP 200 – valid number pairs
# ---------------------------------------------------------------------------

class TestAddSuccess:
    """Five or more valid (number1, number2) pairs, all returning HTTP 200."""

    @pytest.mark.parametrize("number1, number2, expected", [
        (0,      0,      0),           # zero + zero (OpenAPI example)
        (2,      2,      4),           # integer addition (OpenAPI example)
        (1.5,    2.5,    4.0),         # positive floats
        (-3,    -7,     -10),          # both negative
        (10,    -4,      6),           # mixed sign
        (1e6,   2e6,    3e6),          # large numbers
        (0.1,    0.2,    0.1 + 0.2),   # float precision — use server result
    ])
    def test_valid_pair(self, client, number1, number2, expected):
        response = client.post("/add", json={"number1": number1, "number2": number2})
        assert response.status_code == 200
        body = response.json()
        assert "result" in body
        assert body["result"] == pytest.approx(expected)

    def test_response_content_type_is_json(self, client):
        response = client.post("/add", json={"number1": 1, "number2": 1})
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")

    def test_no_extra_keys_in_success_response(self, client):
        response = client.post("/add", json={"number1": 3, "number2": 4})
        assert response.status_code == 200
        assert set(response.json().keys()) == {"result"}


# ---------------------------------------------------------------------------
# HTTP 400 – missing / null / empty parameters
# ---------------------------------------------------------------------------

class TestAddMissingParameters:
    """Required fields absent → 400 with error message."""

    def test_missing_both_fields(self, client):
        response = client.post("/add", json={})
        assert response.status_code == 400
        assert response.json() == {"error": "number1 and number2 are required"}

    def test_missing_number1(self, client):
        response = client.post("/add", json={"number2": 5})
        assert response.status_code == 400
        assert response.json() == {"error": "number1 and number2 are required"}

    def test_missing_number2(self, client):
        response = client.post("/add", json={"number1": 5})
        assert response.status_code == 400
        assert response.json() == {"error": "number1 and number2 are required"}

    def test_null_number1(self, client):
        response = client.post("/add", json={"number1": None, "number2": 1})
        assert response.status_code == 400
        assert "error" in response.json()

    def test_null_number2(self, client):
        response = client.post("/add", json={"number1": 1, "number2": None})
        assert response.status_code == 400
        assert "error" in response.json()

    def test_empty_json_object_body(self, client):
        """Sending `{}` as raw bytes with JSON content-type."""
        response = client.post(
            "/add",
            content=b"{}",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 400
        assert "error" in response.json()

    def test_completely_empty_body(self, client):
        response = client.post(
            "/add",
            content=b"",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 400
        assert "error" in response.json()


# ---------------------------------------------------------------------------
# HTTP 400 – invalid value types
# ---------------------------------------------------------------------------

class TestAddInvalidTypes:
    """Fields present but not numeric → 400 with error message."""

    @pytest.mark.parametrize("number1, number2", [
        ("abc",   2),          # string first arg
        (2,       "abc"),      # string second arg
        ("foo",   "bar"),      # both strings
        ([1, 2],  2),          # list first arg
        (1,       {"val": 2}), # object second arg
    ])
    def test_invalid_type_returns_400(self, client, number1, number2):
        response = client.post("/add", json={"number1": number1, "number2": number2})
        assert response.status_code == 400
        body = response.json()
        assert "error" in body
        assert isinstance(body["error"], str)
        assert len(body["error"]) > 0

    def test_error_response_has_no_extra_keys(self, client):
        response = client.post("/add", json={"number1": "bad", "number2": 1})
        assert response.status_code == 400
        assert set(response.json().keys()) == {"error"}
