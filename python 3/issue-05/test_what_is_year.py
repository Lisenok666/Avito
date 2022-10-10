from what_is_year_now import what_is_year_now
import pytest
from unittest.mock import patch


def test_format_yyyy_first():
    with patch("what_is_year_now.urllib.request.urlopen") as mocked_urlopen:
        mocked_urlopen.return_value = open('format_yyyy_first.json')
        assert what_is_year_now() == 2022
        mocked_urlopen.assert_called_once()


def test_format_yyyy_last():
    with patch("what_is_year_now.urllib.request.urlopen") as mocked_urlopen:
        mocked_urlopen.return_value = open('format_yyyy_last.json')
        assert what_is_year_now() == 1984
        mocked_urlopen.assert_called_once()


def test_raise_ValueError():
    with patch("what_is_year_now.urllib.request.urlopen") as mocked_urlopen:
        mocked_urlopen.return_value = open('bad_format.json')
        with pytest.raises(ValueError):
            what_is_year_now()
