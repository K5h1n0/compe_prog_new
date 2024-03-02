import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

n = int(input())

@lru_cache(maxsize=10000)
def f(x):
    if x == 1:
        return 0
    elif x == 2:
        return 2
    else:
        next1 = x//2
        next2 = (x+2-1)//2
        return x + f(next1) + f(next2)


print(f(n))