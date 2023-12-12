from collections import defaultdict

n,k = map(int,input().split())
l = []
date = []
total = 0
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
    date.append(a)
    total += b
d = defaultdict(int)
date.sort()
d2 = defaultdict(int)
for i,v in enumerate(date):
    d[v] = i+1
    d2[i+1] = v
tmp = [0]*(n+1)
tmp[0] = total
for i in l:
    tmp[d[i[0]]] -= i[1]
for i in range(1,len(tmp)):
    tmp[i] += tmp[i-1]
for i in range(len(tmp)):
    if tmp[i] <= k:
        print(d2[i]+1)
        exit()