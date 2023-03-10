"""
Contains functions that affect Google Groups
"""
from .buildservice import build_google_service


def add_emails_to_group(group_id: str, emails: list[str]) -> None:
    """
    This function takes a Google Group ID and a list of emails and adds the emails to
    the group.

    Args:
        group_id (str): The Google Group ID of the group to add members to
        emails (list): List of emails to add to the group
    """

    service = build_google_service("groupssettings", "v1")
    for email in emails:
        response = (
            service.members()
            .insert(groupUniqueId=group_id, body={"email": email, "role": "MEMBER"})
            .execute()
        )
        print(response)
