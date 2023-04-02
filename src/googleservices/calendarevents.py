"""
Contains functions that affect Google Calendar
"""
from dataclasses import dataclass

from .buildservice import build_google_service


@dataclass
class CalendarEvent:
    """Represents a calendar event.

    - id (str): The id of the calendar event
    - name (str): The name of the caledar event. By default in English.
    - start_time (str): The start time of the calendar event. Recurring calendar events have the original start time.
    - end_time (str): The end time of the calendar event. Recurring calendar events have the original end time.

    """

    name: str
    id: str
    start_time: str
    end_time: str


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
        service.events().list(calendarId=calendar_id, singleEvents=False).execute()
    )
    event_items = events_result.get("items", [])
    events: list[CalendarEvent] = []
    for item in event_items:
        events.append(
            CalendarEvent(
                id=item["id"],
                name=item.get("summary", ""),
                start_time=item["start"]["dateTime"],
                end_time=item["end"]["dateTime"],
            )
        )

    return events


def update_calendar_event_participants(
    calendar_id: str, event_id: str, participants: list[str]
) -> None:
    """
    This function updates the participants of a Google Calendar event.

    Participants will receive notifications that they have been invited to the event.

    Args:
        calendar_id (str): The calendar ID of the calendar to update
        event_id (str): The ID of the event to update
        participants (list[str]): List of participant email addresses

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """
    participants_body = [{"email": email} for email in participants]

    service = build_google_service("calendar", "v3")
    service.events().patch(
        calendarId=calendar_id,
        eventId=event_id,
        body={"attendees": participants_body},
        sendUpdates="all",
    ).execute()
