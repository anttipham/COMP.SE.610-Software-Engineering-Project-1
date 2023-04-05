"""
Utility and helper functions for googleservices package
"""
from typing import TypeVar
from urllib.parse import parse_qs, urlparse

import requests

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


def json_to_Response(json_file: str, status_code: int) -> requests.Response:
    """
    Helper function to convert json file to a requests.Response object

    This will be used to mock the response from the API

    :param json_file: path to the json file
    :param status_code: status code to give to the mock response

    :return: mock response object made from the given json file and status code
    """

    with open(json_file, "rb") as file:
        data = file.read()

    mock_response = requests.Response()
    mock_response._content = data
    mock_response.status_code = status_code

    return mock_response
