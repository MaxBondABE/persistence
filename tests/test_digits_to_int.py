import pytest
from tests.constants import BAD_TYPES

from persistence.core import digitsToInt

@pytest.mark.parametrize("testcase", BAD_TYPES)
def test_digts_to_int_rejects_bad_types(testcase):
    with pytest.raises(TypeError):
        digitsToInt(testcase)

@pytest.mark.parametrize("testcase", (
    (11, ),
    (11, 5),
    (5, 11)
))
def test_digts_to_int_rejects_digits_greater_than_9(testcase):
    with pytest.raises(ValueError):
        digitsToInt(testcase)

@pytest.mark.parametrize("testcase", (
    (-5, ),
    (5, -5),
    (-5, 5)
))
def test_digts_to_int_rejects_negative_digits(testcase):
    with pytest.raises(ValueError):
        digitsToInt(testcase)

examples = {
    (2,): 2,
    (0, 2): 2,
    (1, 0, 0): 100,
    (9,)*1000: 10**1000-1,
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_digts_to_int_properly_processes_input(testcase, expected):
    assert digitsToInt(testcase) is expected
