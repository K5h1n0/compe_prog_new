from collections import defaultdict

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = sorted(a+b)
d = defaultdict(int)
for i,v in enumerate(c):
    d[v] = i+1
aans = []
bans = []
for i in a:
    aans.append(d[i])
for i in b:
    bans.append(d[i])
print(*aans)
print(*bans)