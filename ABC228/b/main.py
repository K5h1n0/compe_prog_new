import sys
sys.setrecursionlimit(10**6)

n,x = map(int,input().split())
a = list(map(int,input().split()))
l = [0] * n

def f(b):
    if l[b-1] == 0:
        l[b-1] = 1
        f(a[b-1])

f(x)
print(sum(l))