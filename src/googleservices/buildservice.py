import google.auth
from googleapiclient.discovery import build, Resource
import environ


def build_google_service(api_name: str, api_version: str) -> Resource:
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
        return build(api_Name, api_version, credentials=cred)

    # Handle other errors.
    except:
        print("Not implemented! Handles all other errors.")
