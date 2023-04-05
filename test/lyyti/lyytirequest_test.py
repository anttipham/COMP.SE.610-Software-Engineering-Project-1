"""
Tests for the functions in src/lyytirequest.py
"""

import json
from unittest.mock import patch

import requests

from lyyti.lyytirequest import generate_headers, get_events, get_participants


def json_to_Response(json_file: str, status_code: int) -> requests.Response:
    """
    Helper function to convert json file to a requests.Response object
    """
    with open(json_file, "rb") as file:
        data = file.read()

    example_response = requests.Response()

    # print(data)

    example_response._content = data
    example_response.status_code = status_code

    print(example_response.json())


json_to_Response(
    "C:/Users/Milo Brown/Desktop/School/3.vuosi/periodi3/SEP1/COMP.SE.610-Software-Engineering-Project-1/res/events-sample.json",
    200,
)


def test_generate_headers() -> None:
    """
    Test if generate_headers returns a dict with correct keys
    """
    headers = generate_headers("call_string")
    assert isinstance(headers, dict)
    assert "Accept" in headers
    assert "Authorization" in headers


def test_generate_headers_accept() -> None:
    """
    Test if generate_headers returns a dict with correct Accept key
    """
    headers = generate_headers("call_string")
    assert headers["Accept"] == "application/json; charset=utf-8"


class TestGetEvents:
    """
    Test class for get_events function
    """

    def test_get_events_succeeds(self) -> None:
        """
        Test if get_events call to API endpoint succeeds
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.ok = True

            response = get_events()
            assert response.ok

    def test_get_events_fails(self) -> None:
        """
        Test if get_events call to API endpoint fails
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.ok = False

            response = get_events()
            assert response.ok == False

    def test_get_events_json(self) -> None:
        """
        Test if get_events call to API endpoint returns json
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            # use sample data from res/events-sample.json
            with open("res/events-sample.json", "r") as file:
                data = json.load(file)
                mock_get.return_value.json.return_value = data

            response = get_events()
            assert response.json() == data

    def test_get_events_status_code(self) -> None:
        """
        Test if get_events call to API endpoint returns status code
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.status_code = 200

            response = get_events()
            assert response.status_code == 200

    def test_get_events_url(self) -> None:
        """
        Test if get_events call to API endpoint returns correct url
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.url = "https://api.lyyti.fi/v1/events"

            response = get_events()
            assert response.url == "https://api.lyyti.fi/v1/events"


class TestGetParticipants:
    """Test class for get_participants function"""

    def test_get_participants_succeeds(self) -> None:
        """
        Test if get_participants call to API endpoint succeeds
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.ok = True

            response = get_participants("event_id")
            assert response.ok

    def test_get_participants_fails(self) -> None:
        """
        Test if get_participants call to API endpoint fails
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.ok = False

            response = get_participants("event_id")
            assert response.ok == False

    def test_get_participants_json(self) -> None:
        """
        Test if get_participants call to API endpoint has json in payload
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            # use sample data from res/participants-sample.json
            with open("res/participants-sample.json", "r") as file:
                data = json.load(file)
                mock_get.return_value.json.return_value = data

            response = get_participants("event_id")
            assert response.json() == data

    def test_get_participants_status_code(self) -> None:
        """
        Test if get_participants call to API endpoint returns status code
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.status_code = 200

            response = get_participants("event_id")
            assert response.status_code == 200

    def test_get_participants_url(self) -> None:
        """
        Test if get_participants call to API endpoint returns correct url
        Creates a mock get request to avoid actual calls to the API
        """
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value.url = (
                "https://api.lyyti.fi/v1/events/event_id/participants"
            )

            response = get_participants("event_id")
            assert (
                response.url == "https://api.lyyti.fi/v1/events/event_id/participants"
            )
