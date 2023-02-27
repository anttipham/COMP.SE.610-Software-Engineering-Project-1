"""
Tests for the functions in src/lyytirequest.py
"""

from unittest.mock import patch

from lyyti import lyytirequest


def test_get_events() -> None:
    """Test if get_events call to API endpoint succeeds"""
    with patch("lyyti.lyytirequest.requests.get") as mock_get:
        # response = lyytirequest.get_events()
        # status_code = response.status_code
        mock_get.return_value.ok = True

        response = lyytirequest.get_events()
        assert response.ok
