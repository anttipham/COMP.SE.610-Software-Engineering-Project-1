import google.auth
from google.auth.transport.requests import AuthorizedSession
import os


def send_http_get_request(url: str) -> google.auth.transport.requests._Response:
    """
    Sends get request and returns the response.
    Args:
            url (str): Contains request url.
    Returns:
            google.auth.transport.requests.Response: Contains information from the server.
    """
    try:
        # Get credentials.
        credentials = google.auth.default(
            scopes=[
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/calendar.events",
                "https://www.googleapis.com/auth/admin.directory.group",
            ]
        )[0]

        # Get session.
        authed_session = AuthorizedSession(credentials)

        # Send get request.
        response = authed_session.get(url)

        # Check status code of the response.
        if response.status_code not in range(200, 300):
            raise Exception("Not implemented! request wasnt successful")

        # Return response.
        return response

    # Handle credential errors.
    except google.auth.exceptions.DefaultCredentialsError:
        print(
            "Not implemented! Happened because google credentials are missing or invalid."
        )

    # Handle other errors.
    except:
        print("Not implemented! Handles all other errors.")


def send_http_put_request(
    url: str, updated: str
) -> google.auth.transport.requests._Response:
    """
    Sends put http request to update already existing item.

    Args:
            url (str): Contains request url.
            updated (str): Contains a key-value object in string format

    Returns:
            google.auth.transport.requests.Response: Contains information from the server.
    """
    try:
        # Get credentials.
        credentials = google.auth.default(
            scopes=[
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/calendar.events",
            ]
        )[0]

        # Get session.
        authed_session = AuthorizedSession(credentials)

        # Send get request.
        response = authed_session.put(url, data=updated)

        # Check status code of the response.
        if response.status_code not in range(200, 300):
            raise Exception("Not implemented! request wasnt successful")

        return response

    # Handle credential errors.
    except google.auth.exceptions.DefaultCredentialsError:
        print(
            "Not implemented! Happened because google credentials are missing or invalid."
        )

    # Handle other errors.
    except:
        print("Not implemented! Handles all other errors.")
