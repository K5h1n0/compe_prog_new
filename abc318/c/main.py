n, d, p = map(int, input().split())
f = sorted(list(map(int, input().split())), reverse=True)
now = d
total = 0
ans = 0
for i in range(n):
    now = (now-1) % d
    total += f[i]
    if now == 0:
        if p < total:
            ans += p
        else:
            ans += total
        total = 0
if p < total:
    ans += p
else:
    ans += total
print(ans)
