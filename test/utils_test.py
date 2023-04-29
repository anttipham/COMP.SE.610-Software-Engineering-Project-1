"""
Tests for the functions in utils module.
"""
import pytest

from utils import extract_group_id


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

