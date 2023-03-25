"""
Univincity-throw-in-bot
"""
import dataclasses
import json

from environ import set_environ
import lyyti
import googleservices
import utils


def update_google_services(event_list: list[Event]) -> None:
    """
    Updates google group member and google group calendar events participants.

    Args:
        event_list (list[Event]): The lyyti events that contains link to a google group and google calendar.
    """
    ## For each event in events from lyyti.
    for lyyti_event in lyyti_event_list:

        ## Get emails of lyyti event participants.
        lyyti_event_participants_email_list = [
            participant.email for participant in lyyti_event.participants
        ]

        ## Get google group id and google calendar id.
        google_group_id = utils.extract_group_id(lyyti_event.google_group_link)
        google_calendar_id = utils.extract_calendar_id(lyyti_event.google_calendar_link)

        ## Get all calendar events from google calendar.
        google_calendar_events = googleservices.get_calendar_events(google_calendar_id)

        ## Update google calendar events' participants.
        for google_event in google_calendar_events:
            googleservices.update_calendar_event_participants(
                google_calendar_id, google_event.id, lyyti_event_participants_email_list
            )

        ## Update google group members.
        googleservices.update_group_members(
            google_group_id, lyyti_event_participants_email_list
        )


def main():
    """
    Main function
    """

    ## Get all events from lyyti.
    lyyti_event_list = lyyti.load_events()
    update_google_services(lyyti_event_list)


if __name__ == "__main__":
    main()
