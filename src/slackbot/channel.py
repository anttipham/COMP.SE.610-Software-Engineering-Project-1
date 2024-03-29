"""
Handles the authentication of Slack API and the use it for inviting and removing of the
participants.

The code presume that the slack bot is already created and the token is stored in the
environment variable USER_TOKEN.

To communicate with the slack api and add or remove the participants from specific
channel, we need to have following user token scope in the slack bot:
1. channels:read
2. groups:read
3. groups:write
4. users:read
5. users:read.email
6. admin.conversations:write
"""
import os
import slack

client = slack.WebClient(token=os.environ["USER_TOKEN"])


def get_all_user_ids(emails: list[str]) -> set[str]:
    """
    Get all the user Ids from the Workspace
    that match the email addresses in the input list.
    Return a set of IDs.
    Args:
        email (str): The email to use

    Returns:
        list[str]:  Gets all the user Ids from the Workspace
    """
    id_set = set()
    for email in emails:
        response = client.users_lookupByEmail(email=email)
        id_set.add(response["user"]["id"])
    return id_set


def get_user_ids_from_channel(channel_id: str) -> set[str]:
    """
    Get all the user IDs from a specific channel.
    Return a set of user IDs.
    Args:
        channelId (str): The Channel Id.

    Returns:
        list[str]:  Return lists of user Ids that are already invited to the channel
    """
    response = client.conversations_members(channel=channel_id)
    member_ids = response["members"]
    return set(member_ids)


def invite_members(emails: list[str], channel_id: str):
    """
    Invite all the users with their email addresses to a specific channel.
    Args:
        emailList list[str]: The list of the email address.
        channelId (str): The Channel Id.

    Returns:
        list[str]:  Return lists of user Ids that are already invited to the channel
    """
    all_id_set = get_all_user_ids(emails)
    members_in_channel_set = get_user_ids_from_channel(channel_id)

    new_members_set = all_id_set - members_in_channel_set
    kicked_members_set = members_in_channel_set - all_id_set

    for member in new_members_set:
        client.admin_conversations_invite(channel=channel_id, user=member)

    for member in kicked_members_set:
        client.conversations_kick(channel=channel_id, user=member)


if __name__ == "__main__":
    invite_members(["email1@example.com", "email2@example.com"], "ABC123")
