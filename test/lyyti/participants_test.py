"""
Tests for function in lyyti.participants.py
"""
import json
from dataclasses import FrozenInstanceError
from unittest.mock import patch

import pytest

from lyyti.events import Event, load_events
from lyyti.participants import *
from utils import json_to_Response

with open("test/res/participants-sample.json", "r") as file:
    PARTICIPANT_JSON = json.load(file)


class TestParticipant:
    def test_Participant(self) -> None:
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
    def test_load_participants(self) -> None:
        """
        Test that load_participants works with example data
        Uses mock data from participants-sample.json to avoid unnecessary API calls
        """

        example_id = next(iter(PARTICIPANT_JSON["results"].keys()))
        with patch("lyyti.participants.get_participants") as mock_get_participants:
            mock_get_participants.return_value = json_to_Response(
                "test/res/participants-sample.json", 200
            )
            participants = load_participants(example_id)

            assert isinstance(participants, Sequence)
            assert isinstance(participants[0], Participant)

    def test_load_participants_bad_response(self) -> None:
        """
        Test that load_participants returns an empty tuple if the response is not 200
        Uses mock data from participants-sample.json to avoid unnecessary API calls
        """

        example_id = next(iter(PARTICIPANT_JSON["results"].keys()))
        with patch("lyyti.participants.get_participants") as mock_get_participants:
            mock_get_participants.return_value = json_to_Response(
                "test/res/participants-sample.json", 404
            )
            with pytest.raises(RuntimeError):
                participants = load_participants(example_id)
