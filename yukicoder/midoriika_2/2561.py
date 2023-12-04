import itertools

n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for v in list(itertools.combinations(a,k)):
    total = sum(v)
    if total%998244353 <= total%998:
        ans += 1
        ans %= 998
print(ans)