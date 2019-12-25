import pytest
from tests.constants import BAD_TYPES
from itertools import permutations

from persistence.core import normalize
from persistence.constants import SINGLE_DIGIT_PRIMES, SINGLE_DIGIT_COMPOSITE_FACTORS

@pytest.mark.parametrize("testcase", BAD_TYPES)
def test_normalize_rejects_bad_types(testcase):
    with pytest.raises(TypeError):
        normalize(testcase)

onesExamples = (
    1,
    11,

    (1, ),
    (1, 1)
)
@pytest.mark.parametrize("testcase", onesExamples)
def test_normalize_rejects_numbers_with_only_ones(testcase):
    with pytest.raises(ValueError):
        normalize(testcase)

zeroesExamples = (
    20,
    202,

    (0, ),
    (0, 0),
    (2, 0),
    (0, 2),
    (2, 0, 2),
    (2, 2, 0),
    (0, 2, 2)
)
@pytest.mark.parametrize("testcase", zeroesExamples)
def test_normalize_rejects_numbers_with_zeroes(testcase):
    with pytest.raises(ValueError):
        normalize(testcase)

impossiblyLargeDigitExamples = (
    (11, ),
    (2, 11),
    (11, 2)
)
@pytest.mark.parametrize("testcase", impossiblyLargeDigitExamples)
def test_normalize_rejects_digits_greater_than_9(testcase):
    with pytest.raises(ValueError):
        normalize(testcase)

negativeDigitExamples = (
    (-2, ),
    (2, -2),
    (-2, 2)
)
@pytest.mark.parametrize("testcase", negativeDigitExamples)
def test_normalize_rejects_negative_digits(testcase):
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
    # Reimplemented digits() so they can be tested seperately

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
def test_normalize_output_is_the_same_regardless_of_order_of_digits(testcase):
    assert normalize(testcase) == behaviourExpected
