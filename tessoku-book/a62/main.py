from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

n,m= map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

searched = [0]*(n+1)

def dfs(now):
    for next in d[now]:
        if searched[next] == 0:
            searched[next] = 1
            dfs(next)

searched[1] = 1
dfs(1)
if sum(searched) == n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")