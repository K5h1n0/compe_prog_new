n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    if k < a[i]:
        ans += a[i] - k
print(ans)