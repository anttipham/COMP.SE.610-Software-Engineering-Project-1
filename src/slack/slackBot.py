import slack
import os
import pip._vendor.requests
from pathlib import Path
from dotenv import load_dotenv

# needed User Token Scopes in slackbot:
# channels:read
# groups:read
# groups:write
# users:read
# users:read.email
# admin.conversations:write


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['USER_TOKEN'])

# you can remove 3 rows abouve if you want to insert your slack token directly to the code
# and use the following row instead. Replace "your token" with your slack bot token
# client = slack.WebClient(token="your token")



# Following method gets all the user Ids from the Workspace that matches the email adresses from 
# lyyti event participant list
# parameter listt is a list of email adresses coresponding the memberlist in lyyti event
# Method returs a list of IDs 
def get_all_user_IDs(listt):
    
    id_list = []
    for email in list:
        response = client.users_lookupByEmail(email=email)
        id_list.append(response['user']['id'])
        

    return id_list

# Following methdod gets all the users IDs from specific channel
# parameter channelId is the channel id from lyyti event where participants 
# needs to be added
# method returns list of IDs of users that are already invited to the channel
def get_user_ids_from_channel(channelId):

    response = client.conversations_members(channel=channelId)
    member_ids = response['members']
    return member_ids

# Following method adds new users to the slack channel that have signed up in lyyti
# and removes users from the slack channel that have removed their participation in lyyti
# parameter emaiList is list of emails corresponding the list of users that signed up in lyyti
# parameter ChannelId is the channel id for the channel that is  used in lyyti event
def invite_members(emaiList, channelId):
    allIdList = get_all_user_IDs(emaiList)
    membersInChannel = get_user_ids_from_channel(channelId)
    
    # following loop removes "duplicant" users so users that are already invited to the channel aren't 
    # invited again
    for i in membersInChannel[:]:
        if i in allIdList:
            membersInChannel.remove(i)
            allIdList.remove(i)
    
    for member in allIdList:
        client.admin_conversations_invite(channel=channelId, user=member)
    
    if membersInChannel:
        for member in membersInChannel:
            client.conversations_kick(channel=channelId, user=member)

    return

if __name__ == "__main__":
    invite_members()
    