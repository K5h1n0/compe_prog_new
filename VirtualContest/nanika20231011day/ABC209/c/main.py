from collections import defaultdict

n = int(input())
c = sorted(list(map(int,input().split())))
d = defaultdict(int)
for i in range(1,len(c)+1):
    d[c[i-1]] += 1
print(d)
