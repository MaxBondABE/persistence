from persistence.constants import SINGLE_DIGIT_COMPOSITE_FACTORS

from functools import reduce, wraps
from sympy.utilities.iterables import multiset_permutations

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

def digitsToInt(n):
    """
    Converts a tuple of digits into an integer.

    n must be a tuple of integers between 0 and 9. Note that zeroes at the beginning
    will not have an effect on the output (01 = 1).
    """
    return sum(map(
        lambda d: d[0] * 10**d[1],
        zip(n, range(len(n)-1, -1, -1)
    )))
        

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

    n = normalize(n)
    paths = set([tuple()])
    queue = [(n, tuple())]

    yield n
    while queue:
        number, path = queue.pop()
        for composite, factors in SINGLE_DIGIT_COMPOSITE_FACTORS.items():
 
            if not False in [
                factors.count(prime) <= number.count(prime)
                for prime in factors
            ]:
                newPath = tuple(sorted(path + (composite, )))
                if not newPath in paths:
                    newNumber = list(number)
                    newNumber.append(composite)
                    for prime in factors:
                        newNumber.remove(prime)
                    newNumber = tuple(newNumber)

                    paths.add(newPath)
                    queue.append((newNumber, newPath))
                    yield newNumber

def reachable(n):
    pass

def equivalentPermutations(n):
    """
    Yields each possible number that can be obtained by combining & rearranging digits of n.
    Numbers obtained in this way are equivalent in that they have the same multiplicative persistence.
    """
    return None

def previous(n):
    """
    Finds a number which comes before n in a a sequence resulting from multiplicative persistence. If
    no such number exists, returns None. Otherwise, returns an integer.

    Every number resulting from multiplying all of the base 10 digits of a number together will have only
    single-digit prime factors. Conversely, for every number who's only prime factors are the single digit
    primes (though they may be a factor more than once), there exist numbers which, when their digits are
    multiplied, will result in that number. (For instance, you can take all of those prime factors & concatenate
    them together.)
    """
    return None

def persistence(n):
    """
    """
    return None
