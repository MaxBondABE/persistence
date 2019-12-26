import pytest
from tests.constants import BAD_TYPES

from persistence.core import enumerateDigits

examples = {
    2: ((2,), ),
    4: ((2, 2), (4, )),
    26: ((2, 2, 3), (4, 3), (2, 6)),
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_enum_digits_properly_processes_input(testcase, expected):
    actual = enumerateDigits(testcase)
    assert set(actual) == set(expected)
    # Compare using sets because the particular order is not specified
    assert len(actual) == len(expected)
    # Catches repeated entries

# TypeErrors and ValueErrors should be caught by normalize() and digits(), so
# until that assumption proves faulty, there's no need to test them here.
