from itertools import permutations
import pytest
from hypothesis import given, assume


from tests.constants import BAD_TYPES
from tests.strategies import digit_tuples
from persistence.core import normalize, persistence
from persistence.constants import SINGLE_DIGIT_PRIMES, SINGLE_DIGIT_COMPOSITE_FACTORS

@pytest.mark.parametrize("testcase", BAD_TYPES)
def test_normalize_rejects_bad_types(testcase):
    with pytest.raises(TypeError):
        normalize(testcase)

impossiblyLargeDigitExamples = (
    (11, ),
    (2, 11),
    (11, 2)
)
@pytest.mark.parametrize("testcase", impossiblyLargeDigitExamples)
def test_normalize_rejects_digit_tuples_greater_than_9(testcase):
    with pytest.raises(ValueError):
        normalize(testcase)

negativeDigitExamples = (
    (-2, ),
    (2, -2),
    (-2, 2)
)
@pytest.mark.parametrize("testcase", negativeDigitExamples)
def test_normalize_rejects_negative_digit_tuples(testcase):
    with pytest.raises(ValueError):
        normalize(testcase)

@pytest.mark.parametrize("testcase", SINGLE_DIGIT_PRIMES)
def test_normalize_correctly_processes_single_digit_primes(testcase):
    assert normalize(testcase) == (testcase, )

@pytest.mark.parametrize("testcase, expected", SINGLE_DIGIT_COMPOSITE_FACTORS.items())
def test_normalize_correctly_processes_single_digit_composites(testcase, expected):
    assert normalize(testcase) == expected

multiDigitExamples = {
    22: (2, 2),
    23: (2, 3),
    24: (2, 2, 2),
    92: (2, 3, 3),
}
@pytest.mark.parametrize("testcase, expected", multiDigitExamples.items())
def test_normalize_correctly_processes_multi_digit_numbers(testcase, expected):
    assert normalize(testcase) == expected

@pytest.mark.parametrize("testcase", range(2, 90, 11))
# Mostly arbitrary set of values which doesn't hit any invalid input
def test_normalize_processes_numbers_and_tuples_identically(testcase):
    assert normalize(testcase) == normalize(tuple(map(int, str(testcase))))
    # Reimplemented digit_tuples() so they can be tested seperately

behaviourExample = (2, 4, 6, 9)
behaviourExpected = (2, 2, 2, 2, 3, 3, 3)

ignoringOnesExample = (
    (1, 2, 4, 6, 9),
    (2, 4, 6, 9, 1),
    (2, 4, 1, 6, 9),
    (2, 1, 4, 1, 6, 1, 9),
    (2, 4, 1, 1, 1, 1, 6, 9),
    (2, 4, 6, 9, 1, 1, 1, 1),
    (1, 1, 1, 1, 2, 4, 6, 9),
)
@pytest.mark.parametrize("testcase", ignoringOnesExample)
def test_normalize_ignores_ones(testcase):
    assert normalize(testcase) == behaviourExpected

@pytest.mark.parametrize("testcase", permutations(behaviourExample))
def test_normalize_output_is_the_same_regardless_of_order_of_digit_tuples(testcase):
    assert normalize(testcase) == behaviourExpected

def test_normalize_correctly_handles_inputs_which_are_all_1s():
    assert normalize(111111) == (0, )

@given(digit_tuples)
def test_normalize_of_numbers_containing_0_is_always_0(testcase):
    assume(0 in testcase)
    assert normalize(testcase) == (0, )

@given(digit_tuples)
def test_normalize_does_not_change_multiplicative_persistence(testcase):
    assert persistence(normalize(testcase)) == persistence(testcase)
