import pytest

from calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_itself():
    assert add("1") == 1


def test_two_numbers_return_sum():
    assert add("1,2") == 3


def test_multiple_numbers_return_sum():
    assert add("1,2,3") == 6


def test_newline_as_delimiter():
    assert add("1\n2,3") == 6


def test_custom_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_number_raises_exception():
    with pytest.raises(Exception) as exc_info:
        add("1,-2,-3")
    assert str(exc_info.value) == "negative numbers not allowed -2,-3"
