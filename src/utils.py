"""
Utility and helper functions for googleservices package
"""


import contextlib
import traceback

from botlog import botlog


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


@contextlib.contextmanager
def tryexceptlog():
    """
    A context manager that catches all exceptions and logs them.
    The execution of the code continues after the with block if an exception was caught.

    The context manager is used as follows:
    ```
    with tryexceptlog():
        # Code that may raise an exception
    ```
    """
    try:
        yield
    except Exception as error:
        botlog(error, traceback.format_exc(), sep="\n")
