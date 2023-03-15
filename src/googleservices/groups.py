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

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """

    service = build_google_service("admin", "directory_v1")
    for email in emails:
        member = {'email': email, 'role': 'MEMBER'}
        service.members().insert(groupKey=group_id, body=member).execute()


def remove_emails_from_group(group_id: str, emails: list[str]) -> None:
    """
    This function takes a Google Group ID and a list of emails and removes the emails from
    the group.

    Args:
        group_id (str): The Google Group ID of the group to remove members from
        emails (list): List of emails to remove from the group

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """
    service = build_google_service('admin', 'directory_v1')

    for email in emails:
        service.members().delete(groupKey=group_id, memberKey=email).execute()
