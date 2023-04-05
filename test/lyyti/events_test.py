import json
from unittest.mock import patch

from lyyti.events import *
from lyyti.participants import Participant
from utils import json_to_Response

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


def test_Event() -> None:
    """Test that dataclass Event works as predicted"""

    example_event = Event(
        event_id="1234",
        name="Example event",
        start_time="2021-01-01T00:00:00+00:00",
        end_time="2021-01-02T00:00:00+00:00",
        participants=[Participant(email="example_email1")],
        google_group_link="example_group_link",
        google_calendar_link="example_calendar_link",
        slack_channel="example_slack_channel",
    )

    assert isinstance(example_event, Event)
    assert isinstance(example_event.event_id, str)
    assert isinstance(example_event.name, str)
    assert isinstance(example_event.start_time, str)
    assert isinstance(example_event.end_time, str)
    assert isinstance(example_event.participants, list)
    assert isinstance(example_event.participants[0], Participant)
    assert isinstance(example_event.google_group_link, str)
    assert isinstance(example_event.google_calendar_link, str)
    assert isinstance(example_event.slack_channel, str)

    # check that end time is later than start time
    assert example_event.end_time > example_event.start_time


def test_parse_custom_field() -> None:
    """Test that parse_custom_field works with example data"""
    # get example data from the res/events-sample.json custom field
    with open("res/events-sample.json", "r") as file:
        data = json.load(file)
        event_id = next(iter(data["results"].keys()))
        example_field = data["results"][event_id]["custom"]

    assert parse_custom_field(example_field) == Custom(
        google_group_link="https://groups.google.com/a/vincit.fi/g/testiryhma-lyytikayttoon/",
        google_calendar_link="https://calendar.google.com/calendar_example/",
        slack_channel="testchannel",
    )


def test_parse_custom_field_empty() -> None:
    """Test that parse_custom_field works with empty data"""
    example_field = {}
    assert parse_custom_field(example_field) == Custom(
        google_group_link="", google_calendar_link="", slack_channel=""
    )


def test_is_in_the_past() -> None:
    """Test that is_in_the_past works as predicted"""
    assert is_in_the_past(1680549351) == True  # this is the timestamp for 03/04/2023
    assert is_in_the_past(32511784551) == False  # this is the timestamp for 04/04/3000


def test_convert_unixtime_to_datetimestring() -> None:
    """Test that convert_unixtime_to_datetimestring works as predicted"""
    assert convert_unixtime_to_datetimestring(1235851100) == "2009-02-28 21:58:20"
    assert convert_unixtime_to_datetimestring(1680296400) == "2023-04-01 00:00:00"


def test_get_from_language_field() -> None:
    """Test that get_from_language_field works as predicted"""
    # get example data from the res/events-sample.json language field
    with open("res/events-sample.json", "r") as file:
        data = json.load(file)
        event_id = next(iter(data["results"].keys()))
        example_field = data["results"][event_id]["name"]

    assert get_from_language_field(example_field) == "Kurssi"


def test_get_from_language_field_empty() -> None:
    """Test that get_from_language_field works with empty data"""
    example_field = {}
    assert get_from_language_field(example_field) == ""


def test_load_events() -> None:
    """
    Test that load_events function works as predicted
    Uses mock get_events function in load_events to prevent unnecessary API calls
    """

    with patch("lyyti.events.get_events") as mock_get_events:
        mock_get_events.return_value = json_to_Response("res/events-sample.json", 200)
        events = load_events()

        assert isinstance(events, list)
        assert isinstance(events[0], Event)


def test_load_events_bad_response() -> None:
    """
    Test that load_events function works as predicted with bad response
    Uses mock get_events function in load_events to prevent unnecessary API calls
    """

    with patch("lyyti.events.get_events") as mock_get_events:
        mock_get_events.return_value = json_to_Response("res/events-sample.json", 400)
        events = load_events()

        assert isinstance(events, list)
        assert len(events) == 0
