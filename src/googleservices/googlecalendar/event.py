from ..googlerequest import send_http_get_request, send_http_put_request


def get_calendar_event_participants(calendar_id: str, event_id: str) -> list:
    return send_http_get_request(
        "https://www.googleapis.com/calendar/v3/calendars/{}/events/{}".format(
            calendar_id, event_id
        )
    ).json()["attendees"]


def update_calendar_event_participants(
    calendar_id: str, event_id: str, attendees: dict
) -> list:
    return send_http_put_request(
        "https://www.googleapis.com/calendar/v3/calendars/{}/events/{}".format(
            calendar_id, event_id
        ),
        str(attendees),
    )


def get_calendar_events(calendar_id: str) -> list:
    return send_http_get_request(
        "https://www.googleapis.com/calendar/v3/calendars/{}/events".format(calendar_id)
    ).json()["items"]
