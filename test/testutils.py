"""
Utility files for testing.
"""

import requests


def json_to_Response(json_file: str, status_code: int) -> requests.Response:
    """
    Helper function to convert json file to a requests.Response object

    This will be used to mock the response from the API

    :param json_file: path to the json file
    :param status_code: status code to give to the mock response

    :return: mock response object made from the given json file and status code
    """

    with open(json_file, "rb") as file:
        data = file.read()

    mock_response = requests.Response()
    mock_response._content = data
    mock_response.status_code = status_code

    return mock_response

