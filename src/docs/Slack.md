# Slack Implementation

Implementation of Slack integration can be done via using the Slack API method. I will try to briefly explain the code mechanism as well as the documentation for the Slack integration here. The reason that we can not implement the Slack integration for adding and removing the candidate is because of not having an enterprise Slack account. Let me show how the code will:

## Slack Authentication
Firstly, we need to have the OAuth & Permissions in the slack api so that we can have the authentication for hitting the endpoint for performing any action that we need to have. To add the OAuth Tokens, we need to add User OAUTh Tokens so that we can perform different actions like adding/removing the user in the public and private channel of slack.

### Step to do this action are as follow:
1. Navigate to the workspace and click on the managed apps.
2. Click on the OAuth & Permissions from the side bar.
3. After this, Add OAuth Tokens for the workspace.
4. Once the token is created, we need to add User Token Scopes so that we can perform the specific actions.

![](images/Screenshot%202023-04-19%20at%2018.56.52.png)

## Get WorkSpace Users
Here is the link from slack official docs on how to make the call and get the lists of people in the channel.
[Get Users from WorkSpace](https://api.slack.com/methods/conversations.members)

Here are the steps to perform the action for getting the list of the users from workSpace:
 1. We need to have this api endpoint with GET request for all the userID list: [API EndPoint](https://slack.com/api/conversations.members).
 2. We need to add the above User OAuth Token as authentication token and in the body, we need to pass the team_id and make the api call.
 3. To make this call, we need to make sure that we have admin.users:read user token Scopes

 ## Get Channel Users
 Here is the link from slack official docs on how to make the call and get the lists of people in the channel.
 [Get Users from Specific Channel](https://api.slack.com/methods/conversations.members)

 Here are the steps to perform the action for getting the list of the users from workSpace:
 1. We need to have this api endpoint with GET request for all the userID list: [API EndPoint](https://slack.com/api/conversations.members)
 2. We need to add the above User OAuth Token as authentication token and in the body, we need to pass the channel id and make the api call.
 3. To make this call, we need to make sure that we have channels:read, groups:read, mpim:read, im:read user token Scopes

 ## Invite Users
Here is the link from slack official docs on how to make the call and add the people in the channel.
[Invite Users](https://api.slack.com/methods/conversations.invite)

Here are the steps to perform the action for the user invite in slack:
 1. We need to have this api endpoint with POST request: [API EndPoint](https://slack.com/api/conversations.invite)
 2. We need to add the above User OAuth Token as authentication token and in the body, we need to pass the team_id and users list to add for the specific channel. Like this:
    ![Image of adding body and authorization token in CRUD operation](images/Screenshot%202023-04-19%20at%2019.11.16.png)
 3. Before hitting the above url, we need to make sure that we have following OAuth Scope in the user token scopes:
    - Channels:write, 
    - Channels:read,
    - groups:write,
    - group:read,
    - mpim:read,
    - im:read,
    - mpim:write, 
    - im:write, 
    - admin.users:read
 4. Once we have that, we will be allowed to hit the above url and we can add the users in the channel. (Note: This is the reason that we are documenting this process as we are
    not able to implement it as we do not have enterprise slack workspace with admin role. But one who has this access is able to perform this action.)

## Remove Users
Here is the link from slack official docs on how to make the call and remove the people in the channel.
[Remove Users](https://api.slack.com/methods/conversations.kick)

Here are the steps to perform the action for the user invite in slack:
 1. We need to have this api endpoint with POST request: [API Endpoint](https://slack.com/api/conversations.kick)
 2. Remaining steps are exactly similar, like inviting the users mentioned above.

# Slack Sample Code
There is a file called:
[slackBot.py](../slack//slackBot.py)
Note: This code is just a sample and it may not work as we can not test it as we do not have the admin role in Slack account and neither we have enterprise account to test it.
