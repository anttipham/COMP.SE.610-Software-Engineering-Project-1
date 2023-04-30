"""
Some examples on how to create tests.

Test file should end with '_test'.
Read this: https://docs.pytest.org/en/7.1.x/getting-started.html
"""
import pytest


def increment(x: int) -> int:  # pylint: disable=invalid-name
    """Increments a number by 1."""
    return x + 1


def raise_error() -> None:
    """Raises SystemExit."""
    raise SystemExit(1)


class TestSample:
    """Class name must start with 'Test'"""

    # def test_wrong():
    #     assert func(3) == 5

    def test_method(self) -> None:
        """Test methods must start with 'test_'"""
        assert increment(3) == 4

    def test_raise_error(self) -> None:
        """Test methods must start with 'test_'"""
        with pytest.raises(SystemExit):
            raise_error()
