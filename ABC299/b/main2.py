from collections import defaultdict

n,t = map(int,input().split())
c = list(map(int,input().split()))
r = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[c[i]].append(r[i])
c_set = set(c)
if t in c_set:
    tmp = d[t]
else:
    tmp = d[c[0]]
tmp.sort(reverse=True)
print(r.index(tmp[0])+1)