"""
Tests for function in lyyti.participants.py
"""
import json
from dataclasses import FrozenInstanceError
from unittest.mock import patch
import pytest

from testutils import json_to_response
from lyyti.participants import Participant, load_participants, Sequence

with open("test/res/participants-sample.json", "r", encoding="utf-8") as file:
    PARTICIPANT_JSON = json.load(file)


class TestParticipant:
    """
    For testing participants
    """

    def test_participant(self) -> None:
        """Test that dataclass Participant works as predicted"""

        example_participant = Participant(
            email="example_email",
        )

        assert isinstance(example_participant, Participant)
        assert isinstance(example_participant.email, str)

    def test_immutable_email(self) -> None:
        """Test that dataclass Participant is immutable"""
        participant = Participant(email="example_email")
        with pytest.raises(FrozenInstanceError):
            participant.email = "please raise an error, pretty please"  # type: ignore


class TestLoadParticipants:
    """
    For testing loading participants
    """

    def test_load_participants(self) -> None:
        """
        Test that load_participants works with example data
        Uses mock data from participants-sample.json to avoid unnecessary API calls
        """

        example_id = next(iter(PARTICIPANT_JSON["results"].keys()))
        with patch("lyyti.participants.get_participants") as mock_get_participants:
            mock_get_participants.return_value = json_to_response(
                "test/res/participants-sample.json", 200
            )
            participants = load_participants(example_id)

            assert isinstance(participants, tuple)
            assert isinstance(participants[0], Participant)

    def test_load_participants_bad_response(self) -> None:
        """
        Test that load_participants returns an empty tuple if the response is not 200
        Uses mock data from participants-sample.json to avoid unnecessary API calls
        """

        example_id = next(iter(PARTICIPANT_JSON["results"].keys()))
        with patch("lyyti.participants.get_participants") as mock_get_participants:
            mock_get_participants.return_value = json_to_response(
                "test/res/participants-sample.json", 404
            )
            with pytest.raises(RuntimeError):
                load_participants(example_id)
