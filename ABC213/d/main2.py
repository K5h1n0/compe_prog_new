from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

n = int(input())
d = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
for i in d:
    d[i].sort()
l = []
visited = [False]*(n+1)


def dfs(now):
    global l
    l.append(now)
    for next in d[now]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            l.append(now)


visited[1] = True
dfs(1)
print(*l)
