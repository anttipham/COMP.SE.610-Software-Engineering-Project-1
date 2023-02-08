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
    Gets the participants from Lyyti API.

    Args:
        event_id (str): _description_

    Returns:
        Participant: _description_
    """
    json_object = get_participants(event_id)
    # return [Participant(email='43242')]
    return [Participant(email=data['email'])
            for data in json_object['results']['55845-715819602']['participants']]
