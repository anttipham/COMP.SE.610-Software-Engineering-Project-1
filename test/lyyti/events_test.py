"""
Tests for the functions in src/events.py
"""

from pytest import MonkeyPatch

from lyyti.events import *
from lyyti.participants import Participant

# def test_custom_class() -> None:
#     """Test that class Custom works like it should"""
#     example_custom = Custom(
#         google_group_link="example_group_link",
#         google_calendar_link="example_calendar_link",
#     )
#     assert example_custom["google_group_link"] == "example_group_link"
#     assert example_custom["google_calendar_link"] == "example_calendar_link"


# def test_event_class() -> None:
#     """Test that dataclass Event works like it should"""

#     example_participants = list[
#         Participant(email="example1@test.com"), Participant(email="example2@test.com")
#     ]

#     example_event = Event(
#         event_id="123",
#         participants=example_participants,
#         google_group_link="example_group_link",
#         google_calendar_link="example_calendar_link",
#     )
#     assert (
#         example_event.event_id == "123"
#         and example_event.participants == example_participants
#         and example_event.google_group_link == "example_group_link"
#         and example_event.google_calendar_link == "example_calendar_link"
#     )


def test_parse_custom_field() -> None:
    """Test the parse_custom_fields function in src/events.py"""
    example_field = {
        "3448": {
            "id": 3448,
            "title": "Google Group link",
            "type": "text",
            "answer": "example_group_link",
        }
    }

    assert parse_custom_field(example_field) == Custom(
        google_group_link="example_group_link", google_calendar_link=""
    )


def test_load_events(monkeypatch: MonkeyPatch) -> None:
    """Test the load_events function in src/events.py"""
    assert type(load_events()) == list
