"""
Test the Lyyti requests for getting events
"""

from lyyti import lyytirequest


def test_get_events():
    """Test if get_events call to API endpoint succeeds"""
    response = lyytirequest.get_events()
    status_code = response.status_code

    assert status_code == 200
