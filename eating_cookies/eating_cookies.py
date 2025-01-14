#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    # Initialize the cache if it wasn't passed it
    if cache == None:
        cache = [0] * (n + 1)

    if n <= 1:
        cache[n] = 1
        return 1
    elif n == 2:
        cache[n] = 2
        return 2
    elif n == 3:
        cache[n] = 4
        return 4
    elif cache[n] != 0:
        # print(n, cache)
        return cache[n]
    else:
        cache[n] = (
            eating_cookies(n - 1, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 3, cache)
        )
        return cache[n]


# original solution without caching
def eating_cookies_slow(n, cache=None):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return (
            eating_cookies_slow(n - 1, cache)
            + eating_cookies_slow(n - 2, cache)
            + eating_cookies_slow(n - 3, cache)
        )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")

