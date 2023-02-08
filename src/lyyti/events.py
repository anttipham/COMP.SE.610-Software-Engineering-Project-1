"""
Handles the events of the Lyyti API.
"""

from dataclasses import dataclass
from .participants import Participant, get_participants
from .lyytirequest import get_events


@dataclass
class Event:
    """Contains information of event"""
    event_id: str
    google_group_link: str
    participants: list[Participant]
    # slack_members: list[str]  # For updating participants in Slack



def load_events() -> list[Event]:
    """
    Returns event information from Lyyti API.

    Returns:
        list[Event]: List of events
    """
    json_object = get_events()

    return [Event(event_id=event,
                  google_group_link='WIP',
                  participants=get_participants(event))
            for event, data in json_object['results'].items()]


if __name__ == '__main__':
    import environ
    load_events()
