"""
Univincity-throw-in-bot
"""
import traceback

import lyyti
import googleservices
import utils
from lyyti import Event
from botlog import botlog


def get_participant_email_list(lyyti_event: Event) -> list[str]:
    """
    Fetches participant emails from a single lyyti event and returns them in a list

    Args:
        lyyti_event (Event): Lyyti event containing information of the participants

    Returns:
        list[str]: List containing participant emails as strings
    """
    # Get emails of lyyti event participants.
    lyyti_event_participants_email_list = [
        participant.email for participant in lyyti_event.participants
    ]
    return lyyti_event_participants_email_list


def update_calendar_event_participants(lyyti_event: Event) -> None:
    """
    Updates google calendar event participants for a single event

    Args:
        lyyti_event (Event): Lyyti event containing information of the participants and
        corresponding google event link

    Raises:
        googleapiclient.errors.HttpError: If the updating event participants fails
        ValueError: if the event doesn't contain google_calendar_id
    """
    lyyti_event_participants_email_list = get_participant_email_list(lyyti_event)
    google_calendar_id = lyyti_event.google_calendar_id

    if not google_calendar_id:
        raise ValueError(f"Missing google_calendar_id from event '{lyyti_event}'")

    # Get all calendar events from google calendar.
    botlog(f"Fetching google calendar events from calendar '{google_calendar_id}'")
    google_calendar_events = googleservices.get_calendar_events(google_calendar_id)
    botlog("Fetched Google calendar events:", google_calendar_events)

    # Update google calendar events' participants.
    botlog("Updating google calendar events' participants...")
    for google_event in google_calendar_events:
        googleservices.update_calendar_event_participants(
            google_calendar_id, google_event.id, lyyti_event_participants_email_list
        )
    botlog("Updated google calendar events' participants")

    # Log the updated google calendar events.
    botlog("Google calendar events after update:", google_calendar_events)


def update_google_group_mebmers(lyyti_event: Event) -> None:
    """
    Updates group members for a single event

    Args:
        lyyti_event (Event): Lyyti event containing information of the participants and
        corresponding google group link

    Raises:
        googleapiclient.errors.HttpError: If the updating group members fails.
        ValueError: if the event doesn't contain google_group_id
    """
    lyyti_event_participants_email_list = get_participant_email_list(lyyti_event)
    google_group_id = utils.extract_group_id(lyyti_event.google_group_link)

    if not google_group_id:
        raise ValueError(f"Missing google_group_id from event '{lyyti_event}'")

    # Get all google group members.
    botlog(f"Fetching google group members from group '{google_group_id}'")
    google_group_members_before = googleservices.get_group_members(google_group_id)
    botlog("Fetched Google group members:", google_group_members_before)

    # Update google group members.
    botlog("Updating google group members...")
    googleservices.update_group_members(
        google_group_id, lyyti_event_participants_email_list
    )

    # Log the updated google group members.
    google_group_members_after = googleservices.get_group_members(google_group_id)
    botlog("Google group members after update:", google_group_members_after)


def main():
    """
    Main function
    """
    # Get all events from lyyti. And call update functions.
    lyyti_event_list = lyyti.load_events()
    for lyyti_event in lyyti_event_list:
        botlog(
            "Handling the following Lyyti event:",
            f"- Lyyti event ID: {lyyti_event.event_id}",
            f"- Event name: {lyyti_event.name}",
            f"- Event start time: {lyyti_event.start_time}",
            f"- Event end time: {lyyti_event.end_time}",
            f"- Event google calendar link: {lyyti_event.google_calendar_id}",
            f"- Event google group link: {lyyti_event.google_group_link}",
            sep="\n",
        )

        if lyyti_event.google_calendar_id:
            try:
                update_calendar_event_participants(lyyti_event)
            except Exception as error:
                botlog(error, traceback.format_exc(), sep="\n")

        if lyyti_event.google_group_link:
            botlog("Updating google group members...")
            try:
                update_google_group_mebmers(lyyti_event)
            except Exception as error:
                botlog(error, traceback.format_exc(), sep="\n")


if __name__ == "__main__":
    main()
