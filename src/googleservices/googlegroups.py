"""
Handles calendar events in Google Groups
"""
from .buildservice import build_google_service


def update_groups(group_id: str, emails: list):
    """Updates google group members"""
    service = build_google_service("groupssettings", "v1")
    for email in emails:
        response = (
            service.members()
            .insert(groupUniqueId=group_id, body={"email": email, "role": "MEMBER"})
            .execute()
        )
        print(response)
