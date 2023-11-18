import sys
sys.setrecursionlimit(10**6)

n = int(input())

def f(x):
    if x == 1:
        return "1"
    return f(x-1) +" "+str(x)+" "+ f(x-1)

print(f(n))