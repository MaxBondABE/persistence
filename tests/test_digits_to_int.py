import pytest
from tests.constants import BAD_TYPES

from persistence.core import digitsToInt

examples = {
    (2,): 2,
    (0, 2): 2,
    (1, 0, 0): 100,
    (9,)*1000: 10**1000-1,
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_digts_to_int_properly_processes_input(testcase, expected):
    assert digitsToInt(testcase) == expected
