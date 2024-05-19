n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
i = 0
now = a[i]
i += 1
while i < n:
    if now + a[i] <= k:
        now += a[i]
        i += 1
    else:
        now = 0
        ans += 1
if now != 0:
    ans += 1
print(ans)