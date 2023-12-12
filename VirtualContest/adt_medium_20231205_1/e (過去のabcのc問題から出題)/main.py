from collections import defaultdict
n = int(input())
p = list(map(int,input().split()))
d = defaultdict(int)
for i in range(1,n+1):
    d[p[i-1]] = i
for i in range(n):
    print(d[i+1],end=" ")