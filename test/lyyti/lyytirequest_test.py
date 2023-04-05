"""
Tests for the functions in src/lyytirequest.py
"""

import json
from unittest.mock import patch

from lyyti.lyytirequest import generate_headers, get_events, get_participants
from utils import json_to_Response

""" Get the sample data from res """

events_string_ok = "res/events-sample.json"
empty_json_string = "res/empty-sample.json"
participants_string = "res/participants-sample.json"


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
        Uses a mock response to avoid actual calls to the API
        """

        mock_response = json_to_Response(events_string_ok, 200)
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value = mock_response

            response = get_events()
            assert response.ok
            assert response.status_code == 200
            assert response.json() == json.load(open(events_string_ok, "r"))

    def test_get_events_fails(self) -> None:
        """
        Test if the get_events call to API endpoint fails
        Uses a mock response to avoid actual calls to the API
        """

        # This json file is just an empty dict
        mock_response = json_to_Response(empty_json_string, 400)
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value = mock_response

            response = get_events()
            assert response.ok == False
            assert response.status_code == 400
            assert response.json() == {}


class TestGetParticipants:
    """Test class for get_participants function"""

    def test_get_participants_succeeds(self) -> None:
        """
        Test if get_participants call to API endpoint succeeds
        Uses a mock response to avoid actual calls to the API
        """

        mock_response = json_to_Response(participants_string, 200)
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value = mock_response

            response = get_participants(1240375)
            assert response.ok
            assert response.status_code == 200
            assert response.json() == json.load(open(participants_string, "r"))

    def test_get_participants_fails(self) -> None:
        """
        Test if get_participants call to API endpoint fails
        Uses a mock response to avoid actual calls to the API
        """

        mock_response = json_to_Response(empty_json_string, 400)
        with patch("lyyti.lyytirequest.requests.get") as mock_get:
            mock_get.return_value = mock_response

            response = get_participants(1240375)
            assert response.ok == False
            assert response.status_code == 400
            assert response.json() == {}
