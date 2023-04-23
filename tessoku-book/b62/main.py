from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
d = defaultdict(list)
q = deque()
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
searched = [0] * (n+1)

def dfs(now:int):
    q.append(now)
    for next in d[now]:
        if next == n:
            q.append(next)
            print(*q)
            exit()
        elif searched[next] == 0:
            searched[next] = 1
            dfs(next)
            q.pop()

searched[1] = 1
dfs(1)