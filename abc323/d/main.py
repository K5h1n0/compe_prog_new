from collections import defaultdict

n = int(input())
d = defaultdict(int)
reserve = set()
for i in range(n):
    s,c = map(int,input().split())
    d[s] = c
    now = 1
    for j in range(31):
        reserve.add(s*now)
        now *= 2
reserve = sorted(list(reserve))
for k in reserve:
    if (not k in d):
        continue
    nowslime = d[k] // 2
    d[k] = d[k]%2
    d[k*2] += nowslime
ans = 0
for k in reserve:
    ans += d[k]
print(ans)