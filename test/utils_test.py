"""
Tests for the functions in utils module.
"""
import contextlib
import io

import pytest

from utils import extract_group_id, tryexceptlog


class TestExtractGroupId:
    """Tests for the extract_group_id function."""

    def test_extract_group_id_with_domain(self) -> None:
        """
        Test that the function returns the correct group ID when the URL
        contains the domain name.
        """
        url = (
            "https://groups.google.com/a/oispahuone.com/g"
            "/univincity-throw-in-bot-test-group"
        )
        expected = "univincity-throw-in-bot-test-group@oispahuone.com"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_without_domain(self) -> None:
        """
        Test that the function returns the correct group ID when the URL does
        not contain the domain name.
        """
        url = "https://groups.google.com/g/univincity-throw-in-bot-test-group"
        expected = "univincity-throw-in-bot-test-group"
        actual = extract_group_id(url)
        assert actual == expected

    def test_extract_group_id_empty_url(self) -> None:
        """Test that the function raises ValueError when the URL is empty."""
        url = ""
        with pytest.raises(ValueError):
            extract_group_id(url)


class TestTryExceptLog:
    """
    Tests for the tryexceptlog function.

    Redirects stdout to a StringIO object
    to capture the output.
    """

    def test_tryexceptlog_no_exception(self) -> None:
        """
        Test that the function works
        as expected with no exception.
        """

        def example_function() -> None:
            print("Hello World!")

        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            with tryexceptlog():
                example_function()

            output = buf.getvalue().strip()
            assert output == "Hello World!"

    def test_tryexceptlog_with_exception(self) -> None:
        """
        Test that the function works
        as expected with an exception.
        """

        def example_function() -> None:
            print(1 / 0)

        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            with tryexceptlog():
                example_function()

            output = buf.getvalue().strip()
            assert "ZeroDivisionError" in output
            assert "Traceback (most recent call last):" in output
