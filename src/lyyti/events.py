"""
Handles the events of the Lyyti API.
"""

from dataclasses import dataclass
from .participants import Participant, load_participants
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

    return [Event(event_id=data['eid'],
                  google_group_link='WIP',
                  participants=load_participants(data['eid']))
            for data in json_object['results'].values()]


if __name__ == '__main__':
    import environ
    print(load_events())
