"""
Contains functions that affect Google Calendar
"""
from .buildservice import build_google_service


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
