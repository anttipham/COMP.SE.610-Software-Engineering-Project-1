# PROJ-S2023-G10-Univincity-throw-in-bot

## Setup

1. Place `univincity-throw-in-bot-018d57429b27.json` to the root of the project
2. Create an empty file `src/environ.py`
3. Copy the content of `src/environ.example.py` and paste it into `src/environ.py`
4. Fill the API keys into `src/environ.py`
5. Run the following command `pip install .`

## prerequisite
Python Version V3.9 or newer

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

## Running in Cloud Run Locally

This instructions apply for visual studio code. 
1. Install Google Cloud Code visual studio code extension.
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
3. Generate requirements.txt file using following command:
```bash
pip freeze > requirements.txt
```
4. From visual studio code navbar select view -> Command Palette or shortly press Ctrl+Shift+P.
5. Type Cloud Code: Run on Cloud Run Emulator


