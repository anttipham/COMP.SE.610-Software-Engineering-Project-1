"""
Utility and helper functions for googleservices package
"""
from urllib.parse import urlparse, parse_qs


def extract_group_id(url: str) -> str:
    """
    Extracts the ID from a Google Groups URL.
    Group ID is defined as the group's email address.

    Args:
        url (str): A Google Groups URL.

    Returns:
        str: The ID extracted from the URL.

    Raises:
        ValueError: If the URL is empty.
    """
    if not url:
        raise ValueError("URL cannot be empty")

    # If the URL ends with a '/', remove it.
    if url.endswith("/"):
        url = url.removeprefix("/")

    # Split the URL by '/' and get the last item.
    url_parts = url.split("/")
    group_id = url_parts[-1]

    return group_id


def extract_calendar_id(calendar_url: str) -> str:
    """
    It takes a Google Calendar URL and returns the calendar ID.

    Args:
        calendar_url (str): The URL of the calendar to embed.

    Returns:
        str: The calendar ID
    """
    # Parse the URL to extract the query parameters
    parsed_url = urlparse(calendar_url)
    query_params = parse_qs(parsed_url.query)

    # Extract the calendar ID from the 'src' parameter
    src_param = query_params.get("src", [])

    if not src_param:
        return ""

    calendar_id = src_param[0]
    return calendar_id


def compare_lists(new: list[str], old: list[str]) -> Tuple[list[str], list[str]]:
    """
    Compares two lists and
    returns list of member's that should be removed
    and list of member's that should be added.

    Args:
        new (list[str]): Contains list of emails of members. Contains the new information.
        old (list[str]): Contains list of emails of members. Contains the old information.

    Returns:
        Tuple[list[str], list[str]]: Returns two lists. First list contains
        emails of members that are missing from the second list. Second list contains list of
        emails of members that are missing from the first list.
    """
    to_be_added = set(old) - set(new)
    to_be_removed = set(new) - set(old)
    return list(to_be_added), list(to_be_removed)
