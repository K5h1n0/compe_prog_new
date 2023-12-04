from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
from1 = [float("INF")]*(n+1)
fromnminus1 = [float("INF")]*(n+1)
fromn = [float("INF")]*(n+1)

def bfs(start,result):
    global d
    visited = [False]*(n+1)
    q = deque()
    visited[start] = True
    cnt = 0
    q.append((start,cnt))
    while q:
        nowv,nowcnt = q.popleft()
        result[nowv] = nowcnt
        for nextv in d[nowv]:
            if visited[nextv] == False:
                visited[nextv] = True
                q.append((nextv,nowcnt+1))
    return result

bfs(1,from1)
bfs(n-1,fromnminus1)
bfs(n,fromn)
route1 = from1[n-1] + fromnminus1[n] + fromn[1]
route2 = from1[n] + fromn[n-1] + fromnminus1[1]
result = min(route1,route2)
if result == float("inf"):
    print(-1)
else:
    print(result)