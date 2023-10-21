from collections import defaultdict
import heapq

n,m = map(int,input().split())
d = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    d[a-1].append((c,b-1))
    d[b-1].append((c,a-1))

shortestlist = [float("INF")]*n
visited = [False]*n
shortestlist[0] = 0
visited[0] = True
q = []
for cost,v in d[0]:
    heapq.heappush(q,(cost,v))
while q:
    nowcost,nowv = heapq.heappop(q)
    if visited[nowv] == True:
        continue
    visited[nowv] = True
    shortestlist[nowv] = nowcost
    for nextcost,nextv in d[nowv]:
        if visited[nextv] == True:
            continue
        heapq.heappush(q,(nowcost+nextcost,nextv))
for i in range(len(shortestlist)):
    if shortestlist[i] == float("INF"):
        print(-1)
    else:
        print(shortestlist[i])
