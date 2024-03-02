from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in range(n):
    d[a[i]] = i+1
ans = []
now = -1
for i in range(n):
    ans.append(d[now])
    now = d[now]
print(*ans)