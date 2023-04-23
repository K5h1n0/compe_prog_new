from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

n,x,y = map(int,input().split())
d = defaultdict(list)
for i in range(n-1):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)
searched = [0]*(n+1)
ans = []

def dfs(now):
    searched[now] = 1
    ans.append(now)
    if now == y:
        print(*ans)
        exit()
    for next in d[now]:
        if searched[next] == 0:
            dfs(next)
            ans.pop()

dfs(x)