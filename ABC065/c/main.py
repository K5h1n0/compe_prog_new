import sys

sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
mod = (10**9)+7

def f(x):
    if x == 1:
        return 1
    return (x*f(x-1))%mod

ans = 0
if abs(n-m) <= 1:
    ans += (f(n) * f(m))%mod
    if n == m:
        ans *= 2
    ans %= mod
print(ans)