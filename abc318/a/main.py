n, m, p = map(int, input().split())
ans = 0
for i in range(n-m+1):
    if i % p == 0:
        ans += 1
print(ans)
