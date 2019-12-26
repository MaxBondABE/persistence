from persistence.constants import SINGLE_DIGIT_COMPOSITE_FACTORS

from functools import reduce, wraps

def acceptsNumber(f):
    """
    Decorator which handles incoming numbers. If the number is an integer, it is converted to a
    tuple of digits.

    Accepts positive integers or typles of digits (integers between 0 and 9).
    """

    @wraps(f)
    def wrapped(n, *args, **kwargs):

        if __debug__:
            if isinstance(n, tuple):
                for d in n:
                    if not isinstance(d, int) or isinstance(d, bool):
                    # isinstance(True, int) == True
                        raise TypeError("n must contain only integers.")
                    elif d < 0:
                        raise ValueError("n must not contain negative numbers.")
                    elif d > 9:
                        raise ValueError("n must not contain digits greater than 9.")
            elif isinstance(n, int) and n < 0:
                raise ValueError("n must be a positive integer.")
            elif not isinstance(n, int) or isinstance(n, bool):
                raise TypeError("n must either be a positive integer or a tuple of digit values.")

        if isinstance(n, int):
            n = digits(n)
        return f(n, *args, **kwargs)

    return wrapped

def digits(n):
    """
    Converts a number into a tuple of it's base 10 digits.

    n must be a positive integer.
    """
    if __debug__:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n must be a postitive integer, not {}.".format(type(n)))
        elif n < 0:
            raise ValueError("n must be positive ({} < 0).".format(n))

    return tuple(map(int, str(n)))

@acceptsNumber
def normalize(n):
    """
    Converts a number into it's simplest form with the same multiplicative persistence by:
    - Removing all 1s
    - Factoring composite digits (eg 6 becomes 23)
    - Sorting the digits

    Returns a tuple.
    n must be a positive integer that contains at least 1 digit which is not 0 or 1,
    or a list or tuple of digits with the same constraint.
    """
    if __debug__:
        if 0 in n:
            raise ValueError("n must not contain the digit 0.")
        if n.count(1) == len(n):
            raise ValueError("n must contain digits other than 1.")

    return tuple(sorted(
        reduce(
            lambda a, b: a+b,
            map(
                lambda d:
                    (d, ) if not d in SINGLE_DIGIT_COMPOSITE_FACTORS else \
                    SINGLE_DIGIT_COMPOSITE_FACTORS[d],
                filter(
                    lambda d: d != 1, 
                    n
                ) 
            )
        )
    ))

def compositeCombinations(n):
    """
    Finds all possible combinations of the digits of n by normalizing n into prime
    digits, and then combining them into composite digits.

    Yields tuples.
    n must be a positive integer that contains at least 1 digit which is not 0 or 1,
    or a list or tuple of digits with the same constraint.
    """
    pass

