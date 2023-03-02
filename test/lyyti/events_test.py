import json
from unittest.mock import patch

from lyyti.events import Custom, Event, load_events, parse_custom_field

"""
Tests for the functions in src/events.py
"""


def test_Custom() -> None:
    """Test that class Custom works as predicted"""
    example_custom = Custom(
        google_group_link="example_group_link",
        google_calendar_link="example_calendar_link",
    )
    assert example_custom["google_group_link"] == "example_group_link"
    assert example_custom["google_calendar_link"] == "example_calendar_link"


def test_parse_custom_field() -> None:
    """Test that parse_custom_field works with example data"""
    example_field = {
        "3448": {
            "id": 3448,
            "title": "Google Group link",
            "answer": "https://groups.google.com/g/example_group_link",
        },
        "3449": {
            "id": 3449,
            "title": "Google Calendar link",
            "answer": "https://calendar.google.com/calendar/u/0/r/eventedit/example_calendar_link",
        },
    }
    assert parse_custom_field(example_field) == Custom(
        google_group_link="https://groups.google.com/g/example_group_link",
        google_calendar_link="https://calendar.google.com/calendar/u/0/r/eventedit/example_calendar_link",
    )


def test_parse_custom_field_empty() -> None:
    """Test that parse_custom_field works with empty data"""
    example_field = {}
    assert parse_custom_field(example_field) == Custom(
        google_group_link="", google_calendar_link=""
    )


def test_load_events() -> None:
    """Test that load_events returns a list of Event objects"""
    with patch("lyyti.events.load_events") as mock_get:
        with open("res/events-sample.json", "r") as file:
            data = json.load(file)
            mock_get.return_value.json.return_value = data
    assert isinstance(load_events(), list)
    assert isinstance(load_events()[0], Event)
    assert isinstance(load_events()[0].event_id, int)
