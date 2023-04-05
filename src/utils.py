"""
Utility and helper functions for googleservices package
"""
from typing import TypeVar
from urllib.parse import urlparse, parse_qs

T = TypeVar("T")


def extract_group_id(url: str) -> str:
    """
    Extracts the ID from a Google Groups URL.
    Group ID is defined as the group's email address.
    The domain is optional and is only included if the group is
    a Google Workspace group.

    Example:
        >>> extract_group_id("https://groups.google.com/a/oispahuone.com/g/univincity-throw-in-bot-test-group")
        "univincity-throw-in-bot-test-group@oispahuone.com"
        >>> extract_group_id("https://groups.google.com/g/univincity-throw-in-bot-test-group")
        "univincity-throw-in-bot-test-group"

    Args:
        url (str): A Google Groups URL.

    Returns:
        str: The ID extracted from the URL.

    Raises:
        ValueError: If the URL is empty.
    """
    if not url:
        raise ValueError("URL cannot be empty")

    # Get the domain name from the URL if it exists
    domain = ""
    if "/a/" in url:
        # Get the part of the URL after "/a/" and before the next "/"
        domain = url.split("/a/")[1].split("/")[0]

    # Get the group name from the URL
    group_name = url.split("/g/")[1].split("/")[0]

    email = f"{group_name}"
    if domain:
        email += f"@{domain}"
    return email


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



