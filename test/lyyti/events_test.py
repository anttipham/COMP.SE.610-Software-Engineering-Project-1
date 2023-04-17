"""
Tests for the functions in src/events.py
"""
import json
from dataclasses import FrozenInstanceError
from unittest.mock import patch

import pytest

from lyyti.events import *
from lyyti.participants import Participant
from utils import json_to_Response

EVENTS_JSON = "test/res/events-sample.json"
EMPTY_EVENTS_JSON = "test/res/empty-sample.json"
PAST_EVENTS_JSON = "test/res/past-events-sample.json"
PARTICIPANTS_JSON = "test/res/participants-sample.json"


class TestCustom:
    def test_Custom(self) -> None:
        """Test that class Custom works as predicted"""
        example_custom = Custom(
            google_group_link="example_group_link",
            google_calendar_id="example_calendar_link",
        )
        assert example_custom["google_group_link"] == "example_group_link"
        assert example_custom["google_calendar_id"] == "example_calendar_link"


class TestEvent:
    @pytest.fixture()
    def example_event(self) -> None:
        return Event(
            event_id="1234",
            name="Example event",
            start_time="2021-01-01T00:00:00+00:00",
            end_time="2021-01-02T00:00:00+00:00",
            participants=(Participant(email="example_email1"),),
            google_group_link="example_group_link",
            google_calendar_id="example_calendar_link",
            slack_channel="example_slack_channel",
        )

    def test_Event(self, example_event) -> None:
        """Test that dataclass Event works as predicted"""

        assert isinstance(example_event, Event)
        assert isinstance(example_event.event_id, str)
        assert isinstance(example_event.name, str)
        assert isinstance(example_event.start_time, str)
        assert isinstance(example_event.end_time, str)
        assert isinstance(example_event.participants, tuple)
        assert isinstance(example_event.participants[0], Participant)
        assert isinstance(example_event.google_group_link, str)
        assert isinstance(example_event.google_calendar_id, str)
        assert isinstance(example_event.slack_channel, str)

        # check that end time is later than start time
        assert example_event.end_time > example_event.start_time

    def test_immutable_event_id(self, example_event) -> None:
        """Test that dataclass Event ID is immutable"""
        with pytest.raises(FrozenInstanceError):
            example_event.event_id = "please raise an error, pretty please"

    def test_immutable_event_name(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.name = "please raise an error, pretty please"

    def test_immutable_event_start_time(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.start_time = "please raise an error, pretty please"

    def test_immutable_event_end_time(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.end_time = "please raise an error, pretty please"

    def test_immutable_event_participants(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.participants = ("please raise an error, pretty please",)

    def test_immutable_event_participants_name(self, example_event) -> None:
        with pytest.raises(TypeError):
            example_event.participants[0] = "please raise an error, pretty please"

    def test_immutable_event_google_group_link(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.google_group_link = ["please raise an error, pretty please"]

    def test_immutable_event_google_calendar_id(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.google_calendar_id = "please raise an error, pretty please"

    def test_immutable_event_slack_channel(self, example_event) -> None:
        with pytest.raises(FrozenInstanceError):
            example_event.slack_channel = "please raise an error, pretty please"


class TestParseCustomField:
    def test_parse_custom_field(self) -> None:
        """Test that parse_custom_field works with example data"""
        # get example data from the res/events-sample.json custom field
        with open(EVENTS_JSON, "r") as file:
            data = json.load(file)
            event_id = next(iter(data["results"].keys()))
            example_field = data["results"][event_id]["custom"]

        assert parse_custom_field(example_field) == Custom(
            google_group_link="https://groups.google.com/a/vincit.fi/g/testiryhma-lyytikayttoon/",
            google_calendar_id="https://calendar.google.com/calendar_example/",
            slack_channel="testchannel",
        )

    def test_parse_custom_field_empty(self) -> None:
        """Test that parse_custom_field works with empty data"""
        example_field = {}
        assert parse_custom_field(example_field) == Custom(
            google_group_link="", google_calendar_id="", slack_channel=""
        )

    def test_parse_custom_field_custom_field_not_dict(self) -> None:
        """Test that parse_custom_field works with empty data"""
        example_field = "not a dict"
        assert parse_custom_field(example_field) == Custom(
            google_group_link="", google_calendar_id="", slack_channel=""
        )


class TestIsInThePast:
    def test_is_in_the_past(self) -> None:
        """Test that is_in_the_past works as predicted"""
        assert (
            is_in_the_past(1680549351) == True
        )  # this is the timestamp for 03/04/2023
        assert (
            is_in_the_past(32511784551) == False
        )  # this is the timestamp for 04/04/3000


class TestConvertUnixtimeToDatetimestring:
    def test_convert_unixtime_to_datetimestring(self) -> None:
        """Test that convert_unixtime_to_datetimestring works as predicted"""
        assert convert_unixtime_to_datetimestring(1235851100) == "2009-02-28 21:58:20"
        assert convert_unixtime_to_datetimestring(1680296400) == "2023-04-01 00:00:00"


class TestGetFromLanguageField:
    def test_get_from_language_field(self) -> None:
        """Test that get_from_language_field works as predicted"""
        # get example data from the res/events-sample.json language field
        with open(EVENTS_JSON, "r") as file:
            data = json.load(file)
            event_id = next(iter(data["results"].keys()))
            example_field = data["results"][event_id]["name"]

        assert get_from_language_field(example_field) == "Kurssi"

    def test_get_from_language_field_empty(self) -> None:
        """Test that get_from_language_field works with empty data"""
        example_field = {}
        assert get_from_language_field(example_field) == ""

    def test_get_from_language_field_default(self) -> None:
        """Test that get_from_language_field returns the default value from ["en"] if it exists"""
        example_field = {"fi": "testi", "en": "test"}
        assert get_from_language_field(example_field) == "test"


class TestLoadEvents:
    def test_load_events(self) -> None:
        """
        Test that load_events function works as predicted
        Uses mock get_events function in load_events to prevent unnecessary API calls
        """

        with patch("lyyti.events.get_events") as mock_get_events:
            mock_get_events.return_value = json_to_Response(EVENTS_JSON, 200)
            with patch("lyyti.participants.get_participants") as mock_get_participants:
                mock_get_participants.return_value = json_to_Response(
                    PARTICIPANTS_JSON, 200
                )
                events = load_events()

                assert isinstance(events, list)
                assert isinstance(events[0], Event)

    def test_load_events_bad_response(self) -> None:
        """
        Test that load_events function works as predicted with bad response
        Uses mock get_events function in load_events to prevent unnecessary API calls
        """

        with patch("lyyti.events.get_events") as mock_get_events:
            mock_get_events.return_value = json_to_Response(EVENTS_JSON, 400)
            with pytest.raises(RuntimeError):
                load_events()

    def test_load_events_with_past_events(self) -> None:
        """
        Test that load_events function works as predicted with past events
        Uses mock get_events function in load_events to prevent unnecessary API calls
        """

        with patch("lyyti.events.get_events") as mock_get_events:
            # this is the same as EVENTS_JSON but with past events
            mock_get_events.return_value = json_to_Response(PAST_EVENTS_JSON, 200)
            with patch("lyyti.participants.get_participants") as mock_get_participants:

                mock_get_participants.return_value = json_to_Response(
                    PARTICIPANTS_JSON, 200
                )
                events = load_events()
                assert len(events) == 0
