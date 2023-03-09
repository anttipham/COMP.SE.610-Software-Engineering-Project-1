import google.auth
from googleapiclient.discovery import build
import environ


def build_google_service(api_Name: str, api_version: str) -> object:
    """
    Sends get request and returns the response.

    Returns:
            object: The google api service build.
    """
    try:
        # Get credentials.
        cred = google.auth.default(
            scopes=[
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/calendar.events",
                "https://www.googleapis.com/auth/apps.groups.settings",
            ]
        )[0]

        # Get session.
        with build(api_Name, api_version, credentials=cred) as service:
            return service

    # Handle other errors.
    except:
        print("Not implemented! Handles all other errors.")
