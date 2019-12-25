import pytest
from tests.constants import BAD_TYPES

from persistence.core import digits

# digits() does not accept tuples, unlike other functions
@pytest.mark.parametrize("testcase", BAD_TYPES + ((1, ), ))
def test_digits_rejects_bad_types(testcase):
    with pytest.raises(TypeError):
        digits(testcase)

def test_digits_rejects_negative_values():
    with pytest.raises(ValueError):
        digits(-999)

examples = {
    0: (0, ),
    1: (1, ),
    10: (1, 0),
    11: (1, 1),
    1234567890: (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_digits_correctly_processes_input(testcase, expected):
    assert digits(testcase) == expected

def test_digits_returns_correct_type():
    assert isinstance(digits(1), tuple)
    assert isinstance(digits(1)[0], int)
