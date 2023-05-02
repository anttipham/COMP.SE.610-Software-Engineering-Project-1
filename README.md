# PROJ-S2023-G10-Univincity-throw-in-bot

## Description

Univincity-throw-in-bot is a tool for automating the management of participants
in Vincit's training events. The tool integrates with Lyyti, Google Calendar,
Google Groups and Slack to automatically add or remove participants from relevant
channels as needed.
Eventually the bot will run periodically in Google Cloud Run environment and update
the participants in each channel.

## Limitations and customer involvement

Unfortunately, we were not able to fully implement the Slack integration or run the bot
periodically in Google Cloud Run due to issues with obtaining necessary access.
As a result, the following limitations apply:

- The bot does not automatically update Slack channels
- The bot must be manually run to update participant information
  in Google Calendar and Google Groups

As agreed, the customer will have acces to the codebase and is responsible for editing
the code as needed once they have the necessary access set up. Our team will provide
documentation and guidance to assist the customer in making any necessary changes.

Please note that any modifications made after delivery may impact the functionality and
reliability of the bot. We encourage the customer to test any changes thoroughly before
deploying them to production.

## Setup

1. Clone the repository to your local machine.
2. Place `univincity-throw-in-bot-018d57429b27.json` to the root of the project
3. Create an empty file `src/environ.py`
4. Copy the content of `src/environ.example.py` and paste it into `src/environ.py`
5. If environment variables are set up else where, you do not need to do this part:
   Fill the API keys into `src/environ.py`
6. Install dependencies: `pip install .`

## Prerequisites

- Python 3.9 or newer
- Basic Python setup (pip, Python files on path etc.)

## Running

```bash
python src/main.py
```

## Testing

Tests use PyTest. Start tests with the following command:

```bash
pytest
```

To see coverage of tests use the following command:

```bash
pytest --cov-report term-missing --cov
```

## Slack Documentation

Visit this [Slack.md](./docs/slack.md) file to view documentation

## Running in Cloud Run Locally

This instructions apply for visual studio code.

1. Install Google Cloud Code extension.
2. Create .vscode/launch.json file. Example file content is illustrated below.

   ```bash
   {
       "configurations": [
           {
               "name": "Cloud Run: Run/Debug Locally",
               "type": "cloudcode.cloudrun",
               "request": "launch",
               "build": {
                   "docker": {
                       "path": "Dockerfile"
                   }
               },
               "image": "bottest",
               "service": {
                   "name": "bottest",
                   "containerPort": 8080,
                   "resources": {
                       "limits": {
                           "memory": "256Mi"
                       }
                   }
               },
               "target": {
                   "minikube": {}
               },
               "watch": true
           }
       ]
   }
   ```

3. Generate requirements.txt file using following command.

```bash
pip freeze > requirements.txt
```

4. From visual studio code navbar select view -> Command Palette or press Ctrl+Shift+P.
5. Type "Cloud Code: Run on Cloud Run Emulator"

   ```bash
   pip freeze > requirements.txt
   ```

6. From visual studio code navbar select view -> Command Palette or press Ctrl+Shift+P.
7. Type "Cloud Code: Run on Cloud Run Emulator"
