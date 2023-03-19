"""
Contains functions that affect Google Groups
"""
from .buildservice import build_google_service
from .utils import list_differences


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
        member = {"email": email, "role": "MEMBER"}
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
    service = build_google_service("admin", "directory_v1")

    for email in emails:
        service.members().delete(groupKey=group_id, memberKey=email).execute()


def get_group_members(group_id: str) -> list[str]:
    """
    This function retrieves all group members

    Args:
        group_id (str): The Google Group ID.

    Returns:
        list[str]: Returns list of members' emails.

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """
    emails = []
    service = build_google_service("admin", "directory_v1")

    request = service.members().list(groupKey=group_id)

    while request:
        response = request.execute()
        emails += [member["email"] for member in response["members"]]
        request = service.members().list_next(request, response)
    return emails


def update_group_members(group_id: str, new: list[str]) -> None:
    """
    Updates group members.

    Args:
        new (list[str]): The list that contains member's emails.

    Raises:
        googleapiclient.errors.HttpError: If the function fails.
    """
    old = get_group_members(group_id)
    to_be_added, to_be_removed = list_differences(old, new)

    add_emails_to_group(group_id, to_be_added)
    remove_emails_from_group(group_id, to_be_removed)
