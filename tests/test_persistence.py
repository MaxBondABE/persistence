import pytest
from hypothesis import given, assume

from persistence.core import persistence
from tests.strategies import digit_tuples

examples = {
    10: 1,
    3778888999: 10,
    277777788888899: 11
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_persistence_calculates_correct_values(testcase, expected):
    assert persistence(testcase) == expected

@given(digit_tuples)
def test_order_of_digits_does_not_change_persistence(testcase):
    assert persistence(testcase) == persistence(testcase[::-1])

@given(digit_tuples)
def test_1_digits_do_not_change_persistence(testcase):
    assume(1 in testcase)
    assert persistence(testcase) == persistence(tuple(filter(
        lambda d: d != 1,
        testcase
    )))

@given(digit_tuples)
def test_0_digits_result_in_persistence_of_1(testcase):
    assume(0 in testcase)
    assert persistence(testcase) == 1
