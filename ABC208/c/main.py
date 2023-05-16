from collections import defaultdict

n,k = map(int,input().split())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i] = k//n
d = dict(sorted(d.items()))
cnt = k%n
for i in d:
    if 0 < cnt:
        d[i] += 1
        cnt -= 1
for i in a:
    print(d[i])