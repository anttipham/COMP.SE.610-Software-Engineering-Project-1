# Slack Implementation

Implementation of Slack integration can be done via using the Slack API method. I will try to briefly explain the code mechanism as well as the documentation for the Slack integration here. The reason that we can not implement the Slack integration for adding and removing the candidate is because of not having an enterprise Slack account. Let me show how the code will:

## Slack Authentication

Firstly, we need to have the OAuth & Permissions in the slack api so that we can have the authentication for hitting the slack method for performing any action that we need to have. To add the OAuth Tokens, we need to add User OAUTh Tokens so that we can perform different actions like adding/removing the user in the public and private channel of slack.

Step to do this action are as follows:

1. Navigate to the workspace and click on the managed apps.
2. Click on the OAuth & Permissions from the side bar.
3. After this, Add OAuth Tokens for the workspace.
4. Once the token is created, we need to add User Token Scopes so that we can perform the specific actions.

![User Token Scopes](/docs/images/UserAuth_Scope.png)
![User Token](/docs/images/UserAuth.png)

## Slack Sample Code

Sample code is in [/src/slack/channel.py](../src/slackbot/channel.py). The code uses Python Slack SDK ([https://slack.dev/python-slack-sdk/](https://slack.dev/python-slack-sdk/)).
Note: This code is just a sample and it may not work as we can't test it as we do not have the admin role in Slack account and neither we have enterprise account to test it.
