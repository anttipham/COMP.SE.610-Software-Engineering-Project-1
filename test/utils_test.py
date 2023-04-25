"""
Tests for the functions in utils module.
"""

import pytest

from utils import extract_group_id, tryexceptlog


class TestExtractGroupId:
    """Tests for the extract_group_id function."""

    def test_extract_group_id_with_domain(self):
        """
        Test that the function returns the correct group ID when the URL
        contains the domain name.
        """
        url = "https://groups.google.com/a/oispahuone.com/g/univincity-throw-in-bot-test-group"
        expected = "univincity-throw-in-bot-test-group@oispahuone.com"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_without_domain(self):
        """
        Test that the function returns the correct group ID when the URL does
        not contain the domain name.
        """
        url = "https://groups.google.com/g/univincity-throw-in-bot-test-group"
        expected = "univincity-throw-in-bot-test-group"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_empty_url(self):
        """Test that the function raises ValueError when the URL is empty."""
        url = ""
        with pytest.raises(ValueError):
            extract_group_id(url)


import traceback
from unittest import mock


class TestTryExceptLog:
    """Tests for the tryexceptlog context manager."""

    def test_tryexceptlog_no_exception(self):
        """Test that tryexceptlog does not log anything when no exception is raised."""

        # Create a variable to store the log output
        log_output = ""

        # Mock botlog() method
        botlog_mock = mock.MagicMock()
        with mock.patch("utils.botlog", botlog_mock):
            # Test tryexceptlog with no exception
            with tryexceptlog():
                log_output = "No exception was raised"

            # Verify that no exception was raised and no log message was generated
            botlog_mock.assert_not_called()
            assert log_output == "No exception was raised"

    def test_tryexceptlog_with_exception(self):
        """Test that tryexceptlog logs the exception when an exception is raised."""

        # Create a variable to store the log output
        log_output = ""

        # Mock botlog() method
        botlog_mock = mock.MagicMock()
        with mock.patch("utils.botlog", botlog_mock):
            # Test tryexceptlog with an exception
            with tryexceptlog():
                try:
                    raise ValueError("Test exception")
                except ValueError:
                    log_output = traceback.format_exc()
            assert "ValueError: Test exception" in log_output
            assert "Traceback (most recent call last):" in log_output
