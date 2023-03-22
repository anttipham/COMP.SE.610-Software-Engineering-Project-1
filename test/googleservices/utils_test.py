"""
Tests for the utils module in the googleservices package.
"""
from urllib.parse import parse_qs, urlparse

import pytest

from googleservices import utils
from lyyti.participants import Participant


def test_extract_group_id() -> None:
    """Tests for the extract_group_id function."""
    # Test with a valid URL
    url = "https://groups.google.com/a/example.com/g/example-group"
    group_id = utils.extract_group_id(url)
    assert group_id == "example-group"

    # Test with a URL that ends with a '/'
    url = "https://groups.google.com/a/example.com/g/example-group/"
    group_id = utils.extract_group_id(url)
    assert group_id == "example-group"

    # Test with an empty URL
    url = ""
    with pytest.raises(ValueError):
        utils.extract_group_id(url)


def test_extract_calendar_id() -> None:
    """Tests for the extract_calendar_id function."""

    # Test with a valid URL
    url = "https://calendar.google.com/calendar/embed?src=example.com_1234567890%40resource.calendar.google.com"
    calendar_id = utils.extract_calendar_id(url)
    assert calendar_id == parse_qs(urlparse(url).query)["src"][0]

    # Test with a URL that doesn't have a 'src' parameter
    url = "https://calendar.google.com/calendar/embed"
    calendar_id = utils.extract_calendar_id(url)
    assert calendar_id == ""


def test_list_differences() -> None:
    """Tests for the list_differences function."""
    old_list = [1, 2, 3, 4, 5, 6]
    new_list = [1, 3, 4, 5, 7, 8]

    # Test with a list of integers
    added, removed = utils.list_differences(old_list, new_list)
    assert set(added) == {7, 8}
    assert set(removed) == {2, 6}

    # Test with empty lists
    old_list = []
    new_list = []
    added, removed = utils.list_differences(old_list, new_list)
    assert added == []
    assert removed == []

    # Test with an empty old list
    old_list = []
    new_list = [1, 2, 3]
    added, removed = utils.list_differences(old_list, new_list)
    assert set(added) == {1, 2, 3}
    assert removed == []

    # Test with an empty new list
    old_list = [1, 2, 3]
    new_list = []
    added, removed = utils.list_differences(old_list, new_list)
    assert added == []
    assert set(removed) == {1, 2, 3}

    # Test with a list of participants
    old_list = [
        Participant(email="example1@gmail.com"),
        Participant(email="example2@gmail.com"),
    ]
    new_list = [
        Participant(email="example1@gmail.com"),
        Participant(email="example3@gmail.com"),
        Participant(email="example2@outlook.com"),
    ]
    added, removed = utils.list_differences(old_list, new_list)
    assert set(added) == {
        Participant(email="example3@gmail.com"),
        Participant(email="example2@outlook.com"),
    }
    assert set(removed) == {Participant(email="example2@gmail.com")}
