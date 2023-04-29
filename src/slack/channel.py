"""
Handles the authentication of Slack API and the use of Slack features to add and remove the participants in the channel.
"""

import slack
import os
import pip._vendor.requests
from pathlib import Path
from dotenv import load_dotenv

"""
To communicate with the slack api and add or remove the participants from specific channel,
we need to have following user token scope in the slackBot:
1. channels:read
2. groups:read
3. groups:write
4. users:read
5. users:read.email
6. admin.conversations:write
"""

# Get credentials.
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ["USER_TOKEN"])
"""
you can remove 3 rows above if you want to insert your slack token directly
to the code and use the following row instead. Replace "your token" with your slack bot token
client = slack.WebClient(token="your token") 
"""


def get_all_user_IDs(email) -> list[str]:
    """
    Following method gets all the user Ids from the Workspace
    that matches the email address from lyyti event participant list parameter emails is a list of email address
    corresponding the member list in lyyti event Method return a list of IDs

    Args:
        email (str): The email to use

    Returns:
        list[str]:  Gets all the user Ids from the Workspace
    """
    id_list = []
    for email in list:
        response = client.users_lookupByEmail(email=email)
        id_list.append(response["user"]["id"])

    return id_list


def get_user_ids_from_channel(channel_id: str) -> list[str]:
    """
    This method gets all the users IDs from specific channel.

    Args:
        channelId (str): The Channel Id.

    Returns:
        list[str]:  Return lists of user Ids that are already invited to the channel
    """
    response = client.conversations_members(channel=channel_id)
    member_ids = response["members"]
    return member_ids


def invite_members(emailList: list[str], channelId: str):
    """
    This method invite all the users with their email address to specific channel.

    Args:
        emailList list[str]: The list of the email address.
        channelId (str): The Channel Id.

    Returns:
        list[str]:  Return lists of user Ids that are already invited to the channel
    """
    all_id_list = get_all_user_IDs(emailList)
    members_in_channel = get_user_ids_from_channel(channelId)

    for i in members_in_channel[:]:
        if i in all_id_list:
            members_in_channel.remove(i)
            all_id_list.remove(i)

    for member in all_id_list:
        client.admin_conversations_invite(channel=channelId, user=member)

    if members_in_channel:
        for member in members_in_channel:
            client.conversations_kick(channel=channelId, user=member)

    return


if __name__ == "__main__":
    invite_members()
