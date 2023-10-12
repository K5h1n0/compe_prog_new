from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d1 = defaultdict(int)
sorteda = sorted(set(a[:]),reverse=True)
for i,v in enumerate(sorteda):
    d1[v] = i
l = []
for i in a:
    l.append(d1[i])

d2 = defaultdict(int)
for i in l:
    d2[i] += 1
l = sorted(d2.items())
for i in range(len(l)):
    print(l[i][1])
for i in range(n-len(l)):
    print(0)