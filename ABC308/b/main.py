from collections import defaultdict

n,m = map(int,input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int,input().split()))
syurui = set(d)
dd = defaultdict(int)
for i in range(m):
    dd[d[i]] = p[i+1]
total = 0
for i in c:
    if i in syurui:
        total += dd[i]
    else:
        total += p[0]
print(total)