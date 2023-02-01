"""
Handles the participants of the Lyyti API.
"""
from dataclasses import dataclass


@dataclass
class Participant:
    """Contains information of a participant"""
    email: str


def get_participants(event_id: str) -> list[Participant]:
    """
    Gets the participants from Lyyti API.

    Args:
        event_id (str): _description_

    Returns:
        Participant: _description_
    """
    return [Participant(email='43242')]
