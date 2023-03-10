"""
Handles the authentication of Google API and the use of google-api-python-client.
"""
import google.auth
from googleapiclient.discovery import build, Resource


def build_google_service(api_name: str, api_version: str) -> Resource:
    """
    It builds a Google service object that can be used to make API calls

    Args:
        api_name (str): The name of the API to use
        api_version (str): The version of the API to use

    Returns:
        Resource: A Resource object that from googleapiclient.discovery
    """
    # Get credentials.
    cred = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/calendar.events",
            "https://www.googleapis.com/auth/apps.groups.settings",
        ]
    )[0]

    # Get session.
    with build(api_name, api_version, credentials=cred) as service:
        return service
