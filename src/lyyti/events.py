"""
Handles the events of the Lyyti API.
"""

from dataclasses import dataclass
from typing import Any
from .participants import Participant, load_participants
from .lyytirequest import get_events


@dataclass
class Event:
    """Contains information of event"""
    event_id: str
    participants: list[Participant]
    google_group_link: str
    # slack_members: list[str]  # For updating participants in Slack


def find_google_group_link(custom: dict[str, dict[str, Any]]) -> str:
    """
    From the given custom field in JSON response, return the Google Group link.
    If there's no Google Group link, returns an empty string.

    Args:
        custom (dict[str, dict[str, Any]]): Custom field

    Returns:
        str: Google Group link if found, otherwise empty string.
    """
    if not custom:
        return ''

    custom_contents = custom['custom'].values()
    for content in custom_contents:
        if content['title'] == 'Google Group link':
            google_group_link = content['answer']
            return google_group_link

    # Couldn't find Google Group link
    return ''


def load_events() -> list[Event]:
    """
    Returns event information from Lyyti API.

    Returns:
        list[Event]: List of events
    """
    json_object = get_events()

    return [Event(event_id=data['eid'],
                  participants=load_participants(data['eid']),
                  google_group_link=find_google_group_link(data['custom']))
            for data in json_object['results'].values()]


if __name__ == '__main__':
    import environ
    print(load_events())
