"""
Handles calendar events in Google Groups
"""

import google.auth
from googleapiclient.discovery import build


def update_groups(group_id: str, emails: list[str]):
    """Gets the calendar events from Google Groups"""
    # Authenticate the API request using your Google Cloud Console credentials
    creds, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/apps.groups.settings"]
    )

    # Create a service object to interact with the Google Groups API
    with build("groupssettings", "v1", credentials=creds) as service:
        # Use the members.insert() method to add the member to the group
        for email in emails:
            response = (
                service.members()
                .insert(groupUniqueId=group_id,
                        body={"email": email, "role": "MEMBER"})
                .execute()
            )
            # Debug: Confirm that the member was added successfully
            print(response)
