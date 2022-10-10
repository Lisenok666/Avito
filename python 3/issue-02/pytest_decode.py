from morse import decode
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
     ('... --- ...', 'SOS'),
     ('... --- ... -----', 'SOS0')]
)
def test_decode(test_input, expected):
    assert decode(test_input) == expected
