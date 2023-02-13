"""
Handles the participants of the Lyyti API.
"""
from dataclasses import dataclass

from .lyytirequest import get_participants


@dataclass
class Participant:
    """Contains information of a participant"""
    email: str


def load_participants(event_id: str) -> list[Participant]:
    """
    Returns event participants' data from Lyyti API.

    Args:
        event_id (str): The event ID that the participant data is gathered from

    Returns:
        Participant: Participants' data in a list
    """
    json_object = get_participants(event_id)
    participant_data = (link['participants'][0]
                        for link in json_object['results'].values())

    return [Participant(email=data['email']) for data in participant_data]
