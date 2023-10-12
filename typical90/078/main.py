from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
ans = 0
for i in d:
    d[i].append(i)
    d[i].sort()
    if d[i][1] == i:
        ans += 1
print(ans)