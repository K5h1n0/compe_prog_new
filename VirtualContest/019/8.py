from collections import deque,defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(list)
for i in range(1,n+1):
    d[i].append(a[i-1])
print(d)