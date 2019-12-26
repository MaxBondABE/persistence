import pytest
from tests.constants import BAD_TYPES

from persistence.core import compositeCombinations


examples = {
    2: ((2,), ),
    4: ((2, 2), (4, )),
    26: ((2, 2, 3), (3, 4), (2, 6)),
    22233357: (
        (2,2,2,3,3,3,5,7), # Do nothing,

        (2,3,3,3,4,5,7), # Combining 2s
        (3,3,3,5,7,8),

        (2,2,3,3,5,6,7), # Combinging 2s and 3s
        (2,3,5,6,6,7),
        (5,6,6,6,7), 

        (2,2,2,3,5,7,9), # Combining 3s

        (2,2,5,6,7,9), # Making 9 & combining 2 & 3

        (2,3,4,5,7,9), # Making 9 & combining 2s
        (3,5,7,8,9),

        (4,5,6,7,9), # Making 9, 6, and 4
        (3,3,4,5,6,7) # 6 and 4

    )
}
@pytest.mark.parametrize("testcase, expected", examples.items())
def test_composite_combinations_properly_processes_input(testcase, expected):
    actual = tuple(
        map(
            lambda a: tuple(sorted(a)), # Order of digits is not specified
            compositeCombinations(testcase)
        )
    )
    assert set(actual) == set(expected)
    # Compare using sets because the particular order is not specified
    assert len(actual) == len(expected)
    # Catches repeated entries

# TypeErrors and ValueErrors should be caught by normalize() and digits(), so
# until that assumption proves faulty, there's no need to test them here.
