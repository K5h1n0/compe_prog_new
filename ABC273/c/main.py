# 解説AC
from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i] += 1
d = sorted(d.items(),reverse=True)
for k,v in d:
    print(v)
for i in range(n-len(d)):
    print(0)