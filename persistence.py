#!/usr/bin/python3 -OO

from functools import reduce
from itertools import permutations
from sys import argv
from multiprocessing import Pool

def digits(n):
    return list(map(int, str(n)))

def listToInt(l):
    return reduce(
        lambda a, b: a+b,
        map(
            lambda a: a[0] * 10**a[1],
            zip(l, range(len(l)-1, -1, -1))
        )
    )

def persistence(n):
    if not isinstance(n, list): n = digits(n)

    count = 0
    while len(n) > 1:
        print(listToInt(n))
        n = digits(reduce(lambda a, b: a*b, n))
        count += 1
    print(listToInt(n))

    return count
    print(n, start, end)

def expand(n):
    if not isinstance(n, list):
        n = digits(n)

    m = {
        9: [3,3],
        8: [2, 2, 2],
        6: [2, 3],
        4: [2, 2],
    }
    for k in m:
        while k in n:
            n.remove(k)
            for i in m[k]:
                n.append(i)

    return listToInt(n)

def reachable(n):
    if not isinstance(n, int):
        n = listToInt(n)

    for i in [2,3,5,7]:
        while n % i == 0:
            n = n//i

    return n == 1

def check(n):
    if isinstance(n, int): n = digits(n)

    for i in permutations(n, len(n)):
        if reachable(i):
            return True, i

    return False, None

def search(n, start=233, end=1000):
    if isinstance(n, int): n = digits(n)
    if isinstance(n, list): n = tuple(n)

    end -= len(n)
    i = start
    while i <= end:
        o = check(n + (1, )*i)
        if o[0]:
            return o
        i += 1

    return False, None

def start(n, start, end, pool):
    p = Pool(pool)

if __name__ == "__main__":
    v = {}
    for i, j in zip(argv[1:], range(len(argv[1:]))):
        v[j] = int(i)
    
    n = v.get(1, 277777788888899)
    start = v.get(2, 233)
    end = v.get(3, 1000)
    pool = v.get(4, 4)

    start(n, start, end, pool)
