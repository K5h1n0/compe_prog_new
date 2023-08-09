#一次元の座標圧縮
#二次元の座標圧縮はABC213-C

from collections import defaultdict

n = int(input())
l1 = []
for i in range(n):
    l1.append(int(input()))
l2 = sorted(list(set(l1[:])))
d = defaultdict(int)
for i,v in enumerate(l2):
    d[v] = i
for i in l1:
    print(d[i])