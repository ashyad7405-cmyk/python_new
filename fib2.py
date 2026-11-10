from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
n = int(input("enter a number"))
print(fib(n))  # Computed instantly using automatic caching
