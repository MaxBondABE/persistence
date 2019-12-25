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
    pass

def enumerateDigits(n):
    """
    Finds numbers with the same multiplicative persistence as n by normalizing n,
    and then finding all of the ways it can group the prime digits into composite
    digits.

    Yields tuples.
    n must be a positive integer that contains at least 1 digit which is not 0 or 1,
    or a list or tuple of digits with the same constraint.
    """
    pass
