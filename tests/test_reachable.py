import pytest
from tests.constants import BAD_TYPES

from persistence.core import reachable

unreachableExamples =(
    11,
    8191,
    11*8191,
    (2**10 * 3**10 * 5**10 * 7**10) + 1,
    (2**10 * 3**10 * 5**10 * 7**10) * 11

)
@pytest.mark.parametrize("testcase", unreachableExamples)
def test_reachable_correctly_identifies_unreachable_numbers(testcase):
    assert reachable(testcase) == (False, None)

reachableExamples = {
    10: (2, 5),
    100: (2, 2, 5, 5),
    (2 * 3 * 5 * 7): (2, 3, 5, 7)
}
@pytest.mark.parametrize("testcase, expected", reachableExamples.items())
def test_reachable_correctly_identifies_reachable_numbers(testcase, expected):
    assert reachable(testcase) == (True, expected)
