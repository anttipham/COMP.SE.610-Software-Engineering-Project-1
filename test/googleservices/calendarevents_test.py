"""Tests for googleservices.calendarevents."""

from unittest import TestCase, mock

import pytest
from googleapiclient.errors import HttpError  # type: ignore

from googleservices.calendarevents import *  # pylint: disable=wildcard-import,unused-wildcard-import


class TestCalendarEvent:
    """Tests for the CalendarEvent dataclass."""

    def test_calendar_event(self) -> None:
        """Test that dataclass CalendarEvent works as predicted."""

        example_event = CalendarEvent(
            id="example_id",
            name="example_name",
            start_time="2021-01-01T00:00:00+00:00",
            end_time="2021-01-02T00:00:00+00:00",
        )

        assert isinstance(example_event, CalendarEvent)
        assert isinstance(example_event.id, str)
        assert isinstance(example_event.name, str)
        assert isinstance(example_event.start_time, str)
        assert isinstance(example_event.end_time, str)


class TestGetCalendarEvents(TestCase):
    """
    Tests for the get_calendar_events function.
    Use mock calls to avoid making actual API calls.
    """

    @mock.patch("googleservices.calendarevents.build_google_service")
    def test_get_calendar_events_successfull(
        self, mock_build_google_service: mock.MagicMock
    ) -> None:
        """Test that the get_calendar_events function works as predicted."""
        # Set up teh mock service
        mock_events_result = {
            "items": [
                {
                    "id": "event1",
                    "summary": "Test Event",
                    "start": {"dateTime": "2023-04-26T10:00:00Z"},
                    "end": {"dateTime": "2023-04-26T11:00:00Z"},
                },
                {
                    "id": "event2",
                    "start": {"dateTime": "2023-04-28T14:00:00Z"},
                    "end": {"dateTime": "2023-04-28T15:00:00Z"},
                },
            ]
        }
        mock_exectue = mock.MagicMock(return_value=mock_events_result)
        mock_service = mock.MagicMock()
        mock_service.events().list().execute = mock_exectue
        mock_build_google_service.return_value = mock_service

        # Call the function being tested
        events = get_calendar_events("example_calendar_id")

        # Check the expected output

        expected_events = [
            CalendarEvent(
                "Test Event", "event1", "2023-04-26T10:00:00Z", "2023-04-26T11:00:00Z"
            ),
            CalendarEvent("", "event2", "2023-04-28T14:00:00Z", "2023-04-28T15:00:00Z"),
        ]

        self.assertEqual(events, expected_events)

    @mock.patch("googleservices.calendarevents.build_google_service")
    def test_get_calendar_events_unsuccessfull(
        self, mock_build_google_service: mock.MagicMock
    ) -> None:
        """
        Test that the get_calendar_events function
        raises an exception if the API call fails.
        Expected: googleapiclient.errors.HttpError.
        """

        # Set up the mock service
        mock_service = mock.MagicMock()
        mock_service.events().list().execute.side_effect = HttpError(
            resp=mock.MagicMock(status=404), content=b"Error"
        )
        mock_build_google_service.return_value = mock_service

        # Call the function being tested
        with pytest.raises(HttpError):
            get_calendar_events("example_calendar_id")


class TestUpdateCalendarEventParticipants(TestCase):
    """
    Tests for the update_calendar_event_participants function.
    Use mock calls to avoid making actual API calls.
    """

    @mock.patch("googleservices.calendarevents.build_google_service")
    def test_update_calendar_event_participants_successfull(
        self, mock_build_google_service: mock.MagicMock
    ) -> None:
        """
        Test that the update_calendar_event_participants
        function works as predicted.
        """
        # Set up the mock service
        mock_exectue = mock.MagicMock()
        mock_service = mock.MagicMock()
        mock_service.events().mock.patch().execute = mock_exectue
        mock_build_google_service.return_value = mock_service

        # Call the function being tested
        update_calendar_event_participants(
            "example_calendar_id",
            "example_event_id",
            ["user1@example.com", "user2@example.com"],
        )

        # Check the expected output
        expected_body = {
            "attendees": [
                {"email": "user1@example.com"},
                {"email": "user2@example.com"},
            ]
        }
        mock_service.events().patch.assert_called_once_with(
            calendarId="example_calendar_id",
            eventId="example_event_id",
            body=expected_body,
            sendUpdates="all",
        )

    @mock.patch("googleservices.calendarevents.build_google_service")
    def test_update_calendar_event_participants_unsuccessfull(
        self, mock_build_google_service: mock.MagicMock
    ) -> None:
        """
        Test that the update_calendar_event_participants
        function raises an exception if the API call fails.
        Expected: googleapiclient.errors.HttpError.
        """

        # Set up the mock service
        mock_service = mock.MagicMock()
        mock_service.events().patch().execute.side_effect = HttpError(
            resp=mock.MagicMock(status=404), content=b"Error"
        )
        mock_build_google_service.return_value = mock_service

        # Call the function being tested
        with pytest.raises(HttpError):
            update_calendar_event_participants(
                "calendar1", "event1", ["user1@example.com", "user2@example.com"]
            )
