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
    # Split the link into its component parts
    parts = url.split("/")
    # Extract the group name from the link
    group_name = parts[-1]
    # Extract the domain from the link
    domain = parts[-3]
    # Construct the email address using the group name and domain
    email = f"{group_name}@{domain}"

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



