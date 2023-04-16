"""
Tests for the functions in utils module.
"""
import pytest
import requests

from utils import extract_calendar_id, extract_group_id, json_to_Response


class TestExtractGroupId:
    """Tests for the extract_group_id function."""

    def test_extract_group_id_with_domain(self):
        """
        Test that the function returns the correct group ID when the URL
        contains the domain name.
        """
        url = "https://groups.google.com/a/oispahuone.com/g/univincity-throw-in-bot-test-group"
        expected = "univincity-throw-in-bot-test-group@oispahuone.com"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_without_domain(self):
        """
        Test that the function returns the correct group ID when the URL does
        not contain the domain name.
        """
        url = "https://groups.google.com/g/univincity-throw-in-bot-test-group"
        expected = "univincity-throw-in-bot-test-group"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_empty_url(self):
        """Test that the function raises ValueError when the URL is empty."""
        url = ""
        with pytest.raises(ValueError):
            extract_group_id(url)


class TestExtractCalendarId:
    """Tests for the extract_calendar_id function."""

    def test_extract_calendar_id(self):
        """Test that the function returns the correct calendar ID."""
        url = "https://calendar.google.com/calendar/embed?src=univincity.fi_12345%40group.calendar.google.com&ctz=Europe%2FHelsinki"
        expected = "univincity.fi_12345@group.calendar.google.com"
        actual = extract_calendar_id(url)
        assert actual == expected

    def test_extract_calendar_id_empty_url(self):
        """Test that the function returns an empty string when the URL is empty."""
        url = ""
        expected = ""
        actual = extract_calendar_id(url)
        assert actual == expected

    def test_extract_calendar_id_no_src_param(self):
        """Test that the function returns an empty string when the URL does not contain the 'src' parameter."""
        url = "https://calendar.google.com/calendar/embed?ctz=Europe%2FHelsinki"
        expected = ""
        actual = extract_calendar_id(url)
        assert actual == expected


class TestJsonToResponse:
    """Tests for the json_to_Response function."""

    def test_json_to_Response(self):
        """Test that the function returns a Response object with the correct status code."""
        json_file = "test/res/events-sample.json"
        status_code = 200
        response = json_to_Response(json_file, status_code)
        assert isinstance(response, requests.Response)
        assert response.status_code == status_code
