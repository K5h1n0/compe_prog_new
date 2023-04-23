from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)

