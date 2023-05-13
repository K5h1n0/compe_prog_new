import sys

sys.setrecursionlimit(10**6)
def factorial(x:int): # 階乗
    if x == 0: return 1
    else: return x * factorial(x-1)

print(factorial(int(input())))