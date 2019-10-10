from timeit import timeit


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


s = timeit("fib(10)", globals=globals(), number=1)
print(f"fib(10) took {s} seconds")
# this is so slow, it's making my computer cry
s = timeit("fib(30)", globals=globals(), number=1)
print(f"fib(30) took {s} seconds")


def fib_iter(num):
    fib = [0, 1]
    for i in range(0, num - 1):
        fib.append(fib[i] + fib[i + 1])
    return fib[-1]


# # much faster
s = timeit("fib_iter(10)", globals=globals(), number=1)
print(f"fib_iter(10) took {s} seconds")

s = timeit("fib_iter(30)", globals=globals(), number=1)
print(f"fib_iter(30) took {s} seconds")

s = timeit("fib_iter(1000)", globals=globals(), number=1)
print(f"fib_iter(1000) took {s} seconds")


cache = {}


def fib_dynam(num):
    global cache
    if num <= 1:
        return num
    elif num in cache:
        return cache[num]
    else:
        cache[num] = fib_dynam(num - 1) + fib_dynam(num - 2)
        return cache[num]


# still slower than iterative?
s = timeit("fib_dynam(10)", globals=globals(), number=1)
print(f"fib_dynam(10) took {s} seconds")

s = timeit("fib_dynam(30)", globals=globals(), number=1)
print(f"fib_dynam(30) took {s} seconds")

s = timeit("fib_dynam(1000)", globals=globals(), number=1)
print(f"fib_dynam(1000) took {s} seconds")
