"""
Some examples on how to create tests.

Test file should end with '_test'.
Read this: https://docs.pytest.org/en/7.1.x/getting-started.html
"""
import pytest


def increment(x):
    """Increments a number by 1."""
    return x + 1


def raise_error():
    """Raises SystemExit."""
    raise SystemExit(1)


class TestSample:
    """Class name must start with 'Test'"""
    # def test_wrong():
    #     assert func(3) == 5

    def test_method(self):
        """Test methods must start with 'test_'"""
        assert increment(3) == 4

    def test_raise_error(self):
        """Test methods must start with 'test_'"""
        with pytest.raises(SystemExit):
            raise_error()


def test_func():
    """Test functions must start with 'test_'"""
    assert 4 == 4