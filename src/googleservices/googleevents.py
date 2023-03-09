from .buildservice import build_google_service


def update_calendar_event_participants(
    calendar_id: str, event_id: str, request_body: dict
):
    """Updates google calendar event participants"""
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
