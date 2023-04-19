"""
Handles HTTP requests to Lyyti API.
"""

import base64
import hashlib
import hmac
import os
import time

import requests


def generate_headers(call_string: str) -> dict[str, str]:
    """
    Generates Lyyti API headers from the given call_string.
    The headers contain 'Accept' and 'Authorization' fields.

    A call string is anything that comes after the Lyyti API root.
    So, 'https://api.lyyti.com/v2/' + call_string is the whole URL path.
    The call string should also contain URL query parameters if they are used.

    Args:
        call_string (str): The part of the URL that comes after the Lyyti API
                           root 'https://api.lyyti.com/v2/'

    Returns:
        dict[str, str]: Returns the authorization header.
    """
    public_key = os.environ["LYYTI_PUBLIC_KEY"]
    private_key = os.environ["LYYTI_PRIVATE_KEY"]
    timestamp = str(int(time.time()))
    msg = ",".join([public_key, timestamp, call_string])

    signature = hmac.new(
        private_key.encode("utf-8"),
        msg=base64.b64encode(msg.encode("utf-8")),
        digestmod=hashlib.sha256,
    ).hexdigest()

    headers = {
        "Accept": "application/json; charset=utf-8",
        "Authorization": f"LYYTI-API-V2 public_key={public_key}, "
        + f"timestamp={timestamp}, "
        + f"signature={signature}",
    }

    return headers


def get_events() -> requests.Response:
    """
    Gets events from Lyyti API using requests package and returns
    the response as requests.Response object

    Returns:
        requests.Response object: contains the response to HTTP request.
    """
    call_string = os.environ["LYYTI_EVENTS_CALLSTRING"]
    url = os.environ["LYYTI_ROOT_URL"] + call_string
    response = requests.get(
        url,
        headers=generate_headers(call_string),
        timeout=float(os.environ["TIMEOUT_DURATION"]),
    )
    return response


def get_participants(event_id: str) -> requests.Response:
    """
    Gets participants from an event by its event ID from Lyyti API using
    requests package and returns the response as requests.Response object.

    Returns:
        requests.Response object: contains the response to HTTP request.
    """
    call_string = os.environ["LYYTI_PARTICIPANTS_CALLSTRING"].format(event_id)
    url = os.environ["LYYTI_ROOT_URL"] + call_string
    response = requests.get(
        url,
        headers=generate_headers(call_string),
        timeout=float(os.environ["TIMEOUT_DURATION"]),
    )
    return response
