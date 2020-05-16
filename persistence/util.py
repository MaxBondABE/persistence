from functools import reduce

def prod(l):
    """
    Accepts an iterable of numbers & multiplies them all together.

    This was added to math in Python 3.8.
    This function will be removed in the future. However, right now 3.8 is
    still quite recent, and many distributions are still using 3.7.
    """
    return reduce(lambda a, b: a*b, l)
