"""
Handles HTTP requests to Lyyti API.
"""
import json
import os

# import requests


def get_events() -> dict:
    """
    Gets events from Lyyti API using requests package and returns the json data
    in dictionaries and lists using json package.

    Returns:
        dict: JSON data in dictionaries and lists.
    """
    # url = os.environ['LYYTI_API_URL']
    # headers = {
    #     'accept': 'application/json',
    #     'public_key': 'apitesti',
    #     'signature': 'apitesti',
    #     'timestamp': '1234567890',
    # }
    # response = requests.get(url,
    #                         headers=headers,
    #                         timeout=float(os.environ['TIMEOUT_DURATION']))
    # return response.json()
    return json.loads(os.environ['LYYTI_API_RESPONSE'])

