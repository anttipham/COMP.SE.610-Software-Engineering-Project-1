""" Tests for functions in googleservices/groups.py """

from unittest import TestCase, mock

import pytest
from googleapiclient.errors import HttpError  # type: ignore

from googleservices.groups import *


class TestAddEmailsToGroup:
    """
    Tests for add_emails_to_group()
    Uses mock for the build_google_service() function
    to avoid making API calls
    """

    @mock.patch("googleservices.groups.build_google_service")
    def test_add_emails_to_group_successfull(self, build_mock: object) -> None:
        """Test that add_emails_to_group() adds emails to group"""

        mock_service = mock.MagicMock()
        mock_response = mock.MagicMock()
        mock_service.members().insert().execute.return_value = mock_response
        build_mock.return_value = mock_service  # type: ignore

        group_id = "test_group_id"
        emails = ["test_email1@test.com", "test_email2@test.com"]
        add_emails_to_group(group_id, emails)

        # Create a list of expected calls to the mock service
        expected_calls = [
            mock.call(),
            mock.call(
                groupKey=group_id,
                body={"email": "test_email1@test.com", "role": "MEMBER"},
            ),
            mock.call().execute(),
            mock.call(
                groupKey=group_id,
                body={"email": "test_email2@test.com", "role": "MEMBER"},
            ),
            mock.call().execute(),
        ]

        # Check that the calls to the mock service are as expected
        mock_service.members().insert.assert_has_calls(expected_calls)

    @mock.patch("googleservices.groups.build_google_service")
    def test_add_emails_to_group_unsuccessfull(self, build_mock: object) -> None:
        """Test that add_emails_to_group() raises exception"""

        mock_service = mock.MagicMock()
        mock_service.members().insert().execute.side_effect = HttpError(
            resp=mock.MagicMock(status=404), content=b"Error"
        )
        build_mock.return_value = mock_service  # type: ignore

        group_id = "test_group_id"
        emails = ["test_email1@test.com", "test_email2@test.com"]

        with pytest.raises(HttpError):
            add_emails_to_group(group_id, emails)


class TestRemoveEmailsFromGroup:
    """
    Tests for remove_emails_from_group()
    Uses mock for the build_google_service() function
    to avoid making API calls
    """

    @mock.patch("googleservices.groups.build_google_service")
    def test_remove_emails_from_group_successfull(self, build_mock: object) -> None:
        """Test that remove_emails_from_group() removes emails from group"""

        mock_service = mock.MagicMock()
        mock_response = mock.MagicMock()
        mock_service.members().delete().execute.return_value = mock_response
        build_mock.return_value = mock_service  # type: ignore

        group_id = "test_group_id"
        emails = [
            "test_email1@test.com",
            "test_email2@test.com",
            "test_email3@test.com",
        ]

        add_emails_to_group(group_id, emails)

        emails_to_remove = ["test_email1@test.com", "test_email3@test.com"]
        remove_emails_from_group(group_id, emails_to_remove)

        # Create a list of expected calls to the mock service
        expected_calls = [
            mock.call(),
            mock.call(groupKey=group_id, memberKey="test_email1@test.com"),
            mock.call().execute(),
            mock.call(groupKey=group_id, memberKey="test_email3@test.com"),
            mock.call().execute(),
        ]

        # Check that the calls to the mock service are as expected
        mock_service.members().delete.assert_has_calls(expected_calls)

    @mock.patch("googleservices.groups.build_google_service")
    def test_remove_emails_from_group_unsuccessfull(self, build_mock: object) -> None:
        """Test that remove_emails_from_group() raises exception"""

        mock_service = mock.MagicMock()
        mock_service.members().delete().execute.side_effect = HttpError(
            resp=mock.MagicMock(status=404), content=b"Error"
        )

        build_mock.return_value = mock_service  # type: ignore

        group_id = "test_group_id"
        emails_to_remove = ["test_email1@test.com", "test_email3@test.com"]

        with pytest.raises(HttpError):
            remove_emails_from_group(group_id, emails_to_remove)


class TestGetGroupMembers(TestCase):
    """
    Tests for get_group_members()
    Uses mock for the build_google_service() function
    to avoid making API calls
    """

    @mock.patch("googleservices.groups.build_google_service")
    def test_get_group_members_successfull(self, build_mock: object) -> None:
        """Test that get_group_members() returns the group members"""

        mock_service = mock.MagicMock()

        mock_members = {
            "members": [
                {"email": "test_email1@test.com"},
                {"email": "test_email2@test.com"},
            ]
        }

        mock_execute = mock.MagicMock()
        mock_execute.execute.return_value = mock_members
        mock_service.members().list.return_value = mock_execute
        mock_service.members().list_next.return_value = None

        build_mock.return_value = mock_service  # type: ignore

        result = get_group_members("test_group_id")
        self.assertEqual(result, ["test_email1@test.com", "test_email2@test.com"])

        build_mock.assert_called_once_with("admin", "directory_v1")  # type: ignore
        mock_service.members().list.assert_called_once_with(groupKey="test_group_id")
        mock_execute.execute.assert_called_once()

    @mock.patch("googleservices.groups.build_google_service")
    def test_get_group_members_unsuccessfull(self, build_mock: object) -> None:
        """Test that get_group_members() raises exception"""

        mock_service = mock.MagicMock()
        mock_service.members().list().execute.side_effect = HttpError(
            resp=mock.MagicMock(status=404), content=b"Error"
        )
        build_mock.return_value = mock_service  # type: ignore

        with self.assertRaises(HttpError):
            get_group_members("test_group_id")


class TestListDifferences:
    """Tests for list_differences()"""

    def test_list_differences_successfull(self) -> None:
        """Test that list_differences() returns the correct lists"""

        test_list1 = ["test_member1", "test_member2", "test_member3"]
        test_list2 = ["test_member1", "test_member2", "test_member4"]

        to_be_added, to_be_removed = list_differences(test_list1, test_list2)
        assert set(to_be_added) == set(["test_member4"])
        assert set(to_be_removed) == set(["test_member3"])

    def test_list_differences_empty_lists(self) -> None:
        """Test that list_differences() returns empty lists"""

        test_list1 = []  # type: ignore
        test_list2 = []  # type: ignore

        to_be_added, to_be_removed = list_differences(test_list1, test_list2)
        assert set(to_be_added) == set([])
        assert set(to_be_removed) == set([])

    def test_list_differences_empty_list1(self) -> None:
        """Test that list_differences() returns empty lists"""

        test_list1 = []  # type: ignore
        test_list2 = ["test_member1", "test_member2", "test_member4"]

        to_be_added, to_be_removed = list_differences(test_list1, test_list2)
        assert set(to_be_added) == set(["test_member1", "test_member2", "test_member4"])
        assert set(to_be_removed) == set([])

    def test_list_differences_empty_list2(self) -> None:
        """Test that list_differences() returns empty lists"""

        test_list1 = ["test_member1", "test_member2", "test_member3"]
        test_list2 = []  # type: ignore

        to_be_added, to_be_removed = list_differences(test_list1, test_list2)
        assert set(to_be_added) == set([])
        assert set(to_be_removed) == set(
            ["test_member1", "test_member2", "test_member3"]
        )


class TestUpdateGroupMembers(TestCase):
    """
    Tests for update_group_members()
    Uses mock for the build_google_service() function
    to avoid making API calls
    """

    @mock.patch("googleservices.groups.get_group_members")
    @mock.patch("googleservices.groups.add_emails_to_group")
    @mock.patch("googleservices.groups.remove_emails_from_group")
    def test_update_group_members_successfull(
        self, remove_mock: object, add_mock: object, get_mock: object
    ) -> None:
        """Test that update_group_members() returns the group members"""

        group_id = "test_group_id"
        old = ["test_email1@test.com", "test_email2@test.com"]
        new = ["test_email2@test.com", "test_email3@test.com"]

        # mock the get_group_members() function
        get_mock.return_value = old  # type: ignore

        # Call the function being tested
        update_group_members(group_id, new)

        # Assert that the correct functions were called
        add_mock.assert_called_once_with(group_id, ["test_email3@test.com"])  # type: ignore
        remove_mock.assert_called_once_with(group_id, ["test_email1@test.com"])  # type: ignore

    @mock.patch("googleservices.groups.update_group_members")
    def test_update_group_members_unsuccessfull(self, update_mock: object) -> None:
        """Test that update_group_members() raises exception"""

        update_mock.side_effect = HttpError(  # type: ignore
            resp=mock.MagicMock(status=404), content=b"Error"
        )

        with self.assertRaises(HttpError):
            update_group_members("test_group_id", ["test_email1@test.com"])
