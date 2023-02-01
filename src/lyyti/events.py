"""
Handles the events of the Lyyti API.
"""

from dataclasses import dataclass
from .participants import Participant, get_participants


@dataclass
class Event:
    """Contains information of event"""
    event_id: str
    google_group_link: str
    participants: list[Participant]
    # slack_members: list[str]  # For updating participants in Slack



def get_events() -> list[Event]:
    """
    Gets the events from Lyyti API.

    Returns:
        list[Event]: List of events
    """
    return [
        Event(event_id='email@tuni.fi',
              google_group_link='link',
              participants=[]),
        Event(event_id='email2@tuni.fi',
              google_group_link='link',
              participants=get_participants('a')),
    ]
