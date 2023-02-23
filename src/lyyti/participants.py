"""
Handles the participants of the Lyyti API.
"""
from dataclasses import dataclass

from .lyytirequest import get_participants


@dataclass(frozen=True)
class Participant:
    """
    Contains information of a participant.

    The participant data is immutable.
    """

    email: str


def load_participants(event_id: str) -> list[Participant]:
    """
    Returns event participants' data from Lyyti API.

    Args:
        event_id (str): The event ID that the participant data is gathered from

    Returns:
        Participant: Participants' data in a list or
        an empty list if http request doesn't succeed
    """
    response = get_participants(event_id)
    status_code = response.status_code
    json_object = response.json()

    participants: list[Participant] = []

    if status_code != 200:
        return participants

    participant_data = (
        link["participants"][0] for link in json_object["results"].values()
    )

    for data in participant_data:
        if data["status"] == "reactedyes":
            participants.append(Participant(email=data["email"]))
    return participants
