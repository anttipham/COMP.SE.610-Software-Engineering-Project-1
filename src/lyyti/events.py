"""
Handles the events of the Lyyti API.
"""

from dataclasses import dataclass
from typing import TypedDict

from .lyytirequest import get_events
from .participants import Participant, load_participants


class Custom(TypedDict):
    """
    Contains custom fields of an event.

    The fields are optional and can be an empty string.
    """

    google_group_link: str
    google_calendar_link: str


@dataclass(frozen=True)
class Event:
    """
    Contains the information of an event.

    google_group_link and google_calendar_link are optional fields and they can
    be an empty string.

    The event data is immutable.
    """

    event_id: str
    participants: list[Participant]
    google_group_link: str
    google_calendar_link: str
    # slack_members: list[str]  # For updating participants in Slack


def parse_custom_field(custom: dict[str, dict[str, str]]) -> Custom:
    """
    From the given custom field in JSON response, return the Google Group link
    and Google Calendar link.

    If there's no Google Group link or Google Calendar link, returns Custom
    with the corresponding field as an empty string.

    If the argument is not a dict, return Custom with empty string in all
    fields.

    Args:
        custom (dict[str, dict[str, str]]): Custom field from Lyyti events

    Returns:
        Custom: Fields are empty strings if not found from args.
    """
    custom_fields = Custom(google_group_link="", google_calendar_link="")

    if not isinstance(custom, dict):
        return custom_fields

    for content in custom.values():
        if content.get("title", "") == "Google Group link":
            custom_fields["google_group_link"] = content.get("answer", "")
        if content.get("title", "") == "Google Calendar link":
            custom_fields["google_calendar_link"] = content.get("answer", "")
    return custom_fields


def load_events() -> list[Event]:
    """
    It loads events from Lyyti API and returns them as a list of Event objects

    Returns:
        list[Event]: List of events or empty list
        if http request doesn't succeed
    """
    response = get_events()
    status_code = response.status_code
    json_object = response.json()

    # print(json.dumps(json_object, indent=2))
    events: list[Event] = []

    if status_code != 200:
        return events

    for data in json_object["results"].values():
        custom_field = parse_custom_field(data["custom"])
        events.append(
            Event(
                event_id=data["eid"],
                participants=load_participants(data["eid"]),
                **custom_field
            )
        )
    return events


if __name__ == "__main__":
    import environ

    print(load_events())
