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
