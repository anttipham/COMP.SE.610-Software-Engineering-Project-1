"""
Handles Slack channels


 Below one is for demo purpose for inviting the users in channel. Once demo is done, it will be removed.
 def add_member():
     ""Adds member to a private Slack channel""
     url = "https://slack.com/api/conversations.invite"

      Hide the below token in env for safety purpose
     auth_token = "xoxp-4651098541781-4653924740979-5138852421297-c007d7f41715a1f2156ecc1334c3d47b"
     headers = {"Authorization": f"Bearer {auth_token}"}
     data = {
         "channel":"C053T5K85RA",
         "users": [ "U053PU7AU7M", "U053HE5BKV4", "U053HE5BKV4", "U053SGL9LLC", "U0539FZMN5V"]
     }

     response = requests.post(url, headers=headers, data=data)
     print(response.status_code)


import requests
from lyyti import get_participants

def get_user_ids_from_workSpace(workSpace):
     ""Get list of User Ids from the workSpace""
     url = "https://slack.com/api/admin.users.list"

    # Hide the below token in env for safety purpose
     auth_token = "xoxp-4651098541781-4653924740979-5138852421297-c007d7f41715a1f2156ecc1334c3d47b"
     headers = {"Authorization": f"Bearer {auth_token}"}
     data = {
        "team_id":"Here, workSpace Id is injecting from the props.",
    }

     response = requests.get(url, headers=headers, data=data)
     # Extract the array of IDs from the response
     members_ids = [user['id'] for user in response['users']]
     print(members_ids)
     return members_ids


def get_user_ids_from_channel(channelId):
     ""Get list of User Ids from the specific channel""
     url = "https://slack.com/api/conversations.members"

    # Hide the below token in env for safety purpose
     auth_token = "xoxp-4651098541781-4653924740979-5138852421297-c007d7f41715a1f2156ecc1334c3d47b"
     headers = {"Authorization": f"Bearer {auth_token}"}
     data = {
        "channel":"Here, channel Id is injecting from the props.",
    }

     response = requests.get(url, headers=headers, data=data)
    # Extract the array of IDs from the response
     members_ids = response['members']
     print(members_ids)
     return members_ids


def invite_users(emailList, channelId):
     ""Invite users to the specific channel""
     url = "https://slack.com/api/conversations.invite"

     # This API EndPoint will fail if we try to invite the users which are already in the channel. So we need to filter the users who are not in channel.
     ## converting the response of list of emails to the sets:

     get_setsOf_user_ids_from_workSpace = set(get_user_ids_from_workSpace("pass here the workSpace id. EG:T04K52WFXNZ"))
     get_setsOf_user_ids_from_channel = set(get_user_ids_from_channel("pass here the channel id. EG:C053M5YP36Z"))

     ## get the list of userID between 2 sets:
     nonInvited_users_list = list(get_setsOf_user_ids_from_workSpace - get_setsOf_user_ids_from_channel)


     # Hide the below token in env for safety purpose
     auth_token = "xoxp-4651098541781-4653924740979-5138852421297-c007d7f41715a1f2156ecc1334c3d47b"
     headers = {"Authorization": f"Bearer {auth_token}"}
     data = {
        "channel":"channelId which is comming as the props",
        "users": "Pass the nonInvited_users_list from above"
    }

     response = requests.post(url, headers=headers, data=data)
     print(response.status_code)


def remove_user(email, channelId):
     ""remove user to the specific channel""
     url = "https://slack.com/api/conversations.kick"

     # This API EndPoint will fail if we try to remove the users which are not in the channel. So we need to filter the users who are in channel only.
     ## converting the response of list of emails to the sets:

     get_setsOf_user_ids_from_workSpace = set(get_user_ids_from_workSpace("pass here the workSpace id. EG:T04K52WFXNZ"))
     get_setsOf_user_ids_from_channel = set(get_user_ids_from_channel("pass here the channel id. EG:C053M5YP36Z"))

     # Use the intersection operation to find the emails that are present in both workSpace and channel
     users_list_in_channel = get_setsOf_user_ids_from_workSpace.intersection(get_setsOf_user_ids_from_channel)

     # Convert the common emails set back to a list
     users_list_in_channel = list(users_list_in_channel)

     for i in users_list_in_channel[:]:
      if users_list_in_channel:
        for user in users_list_in_channel:
            # Hide the below token in env for safety purpose
         auth_token = "xoxp-4651098541781-4653924740979-5138852421297-c007d7f41715a1f2156ecc1334c3d47b"
         headers = {"Authorization": f"Bearer {auth_token}"}
         data = {
        "channel":"channelId which is comming as the props",
        "user": "Pass a user id."
    }

     response = requests.post(url, headers=headers, data=data)
     print(response.status_code)

     return
"""

