#二次元の座標圧縮
#一次元の座標圧縮はABC036-C

from collections import defaultdict

h,w,n = map(int,input().split())
l = []
li = []
lj = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
    li.append(a)
    lj.append(b)
li = sorted(list(set(li)))
lj = sorted(list(set(lj)))
di = defaultdict(int)
dj = defaultdict(int)
for i,v in enumerate(li):
    di[v] = i
for j,v in enumerate(lj):
    dj[v] = j
for i in range(len(l)):
    print(di[l[i][0]]+1,dj[l[i][1]]+1)