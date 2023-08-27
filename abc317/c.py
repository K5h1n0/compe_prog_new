from collections import defaultdict, deque
from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    a, b, c = map(int, input().split())
    d[a].append((b, c))
    d[b].append((a, c))


@lru_cache(maxsize=1000)
def dfs(now, length, visited):
    for next, cost in d[now]:
        if visited[next-1] == 0:
            visited[next-1] = 1
            q.append(cost)
            dfs(next, length+cost, visited)
            q.pop()
            visited[next-1] = 0
    else:
        l.append(sum(q))


ans = []
maximum = 0
for i in range(1, n+1):
    q = deque()
    l = []
    visited_flag = [0]*n
    visited_flag[i-1] = 1
    dfs(i, 0, visited_flag)
    ans.append(max(l))
print()
