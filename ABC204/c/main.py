#解説AC
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6) #おまじないし忘れWA

def dfs(now):
    machi[now] = 1
    for to in d[now]:
        if machi[to] == 0:
            dfs(to)

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)

ans = 0
for i in range(1,n+1):
    machi = [0] * (n+1)
    dfs(i)
    ans += sum(machi)
print(ans)