"""
Univincity-throw-in-bot
"""
import dataclasses
import json

from environ import set_environ
import lyyti
import googleservices
import utils
from lyyti import Event


def get_participant_email_list(lyyti_event: Event) -> list[str]:
    # Get emails of lyyti event participants.
    lyyti_event_participants_email_list = [
        participant.email for participant in lyyti_event.participants
    ]
    return lyyti_event_participants_email_list


def update_calendar_event_participants(lyyti_event: Event) -> None:
    """
    Updates google calendar event participants for a single event

    Args:
        lyyti_event (Event): Lyyti event containing information of the participants and corresponding google event link

    Raises:
        googleapiclient.errors.HttpError: If the updating event participants fails
        ValueError: if the event doesn't contain google_calendar_id
    """
    lyyti_event_participants_email_list = get_participant_email_list(lyyti_event)
    google_calendar_id = utils.extract_calendar_id(lyyti_event.google_calendar_link)

    if not google_calendar_id:
        raise ValueError(f"Missing google_calendar_id from event: {lyyti_event}")

    # Get all calendar events from google calendar.
    google_calendar_events = googleservices.get_calendar_events(google_calendar_id)

    # Update google calendar events' participants.
    for google_event in google_calendar_events:
        googleservices.update_calendar_event_participants(
            google_calendar_id, google_event.id, lyyti_event_participants_email_list
        )


def update_google_group_mebmers(lyyti_event: Event) -> None:
    """
    Updates group members for a single event

    Args:
        lyyti_event (Event): Lyyti event containing information of the participants and corresponding google group link

    Raises:
        googleapiclient.errors.HttpError: If the updating group members fails.
        ValueError: if the event doesn't contain google_group_id
    """
    lyyti_event_participants_email_list = get_participant_email_list(lyyti_event)
    google_group_id = utils.extract_group_id(lyyti_event.google_group_link)

    if not google_group_id:
        raise ValueError(f"Missing google_group_id from event: {lyyti_event}")

    # Update google group members.
    googleservices.update_group_members(
        google_group_id, lyyti_event_participants_email_list
    )


def main():
    """
    Main function
    """

    # Get all events from lyyti. And call update functions.
    lyyti_event_list = lyyti.load_events()
    for lyyti_event in lyyti_event_list:

        update_calendar_event_participants(lyyti_event)
        update_google_group_mebmers(lyyti_event)


if __name__ == "__main__":
    main()
