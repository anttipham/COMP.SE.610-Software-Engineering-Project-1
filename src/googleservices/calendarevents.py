"""
Contains functions that affect Google Calendar
"""
from dataclasses import dataclass

from .buildservice import build_google_service


@dataclass
class CalendarEvent:
    """Represents a calendar event."""

    name: str
    id: str


def get_calendar_events(calendar_id: str) -> list[CalendarEvent]:
    """
    This function takes a Google Calendar ID and returns a list of all events in the
    calendar.

    Args:
        calendar_id (str): The ID of the Google Calendar to fetch events from

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """
    service = build_google_service("calendar", "v3")

    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            singleEvents=False,
            orderBy="startTime",
        )
        .execute()
    )
    event_items = events_result.get("items", [])
    events = [
        CalendarEvent(id=item["id"], name=item["summary"]) for item in event_items
    ]
    return events


def update_calendar_event_participants(
    calendar_id: str, event_id: str, request_body: dict
) -> None:
    """
    This function updates the participants of a Google Calendar event

    Args:
        calendar_id (str): The calendar ID of the calendar to update
        event_id (str): The ID of the event to update
        request_body (dict): TODO: _description_
    """

    service = build_google_service("calendar", "v3")
    response = (
        service.events()
        .update(
            calendarId=calendar_id,
            eventId=event_id,
            body=request_body,
        )
        .execute()
    )
    print(response)
