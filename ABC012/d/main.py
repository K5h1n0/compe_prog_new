from heapq import heappop,heappush

n,m = map(int,input().split())
d = {}
for _ in range(m):
    a,b,cost = map(int,input().split())
    if a not in d:
        d[a] = []
    if b not in d:
        d[b] = []
    d[a].append((cost,b))
    d[b].append((cost,a))
ans = float("inf")
for i in range(1,n+1):
    maximum = 0

    nowshortestlist = [float("inf")]*n
    visited = [False]*n
    visited[i-1] = True
    nowshortestlist[i-1] = 0
    q = []
    for tuple in d[i]:
        heappush(q,tuple)
    while q:
        nowcost,nowv = heappop(q)
        if visited[nowv-1]:
            continue
        visited[nowv-1] = True
        nowshortestlist[nowv-1] = nowcost
        maximum = max(maximum,nowcost)        
        for nextcost,nextv in d[nowv]:
            if visited[nextv-1]:
                continue
            heappush(q,(nowcost+nextcost,nextv))
    ans = min(ans,maximum)
print(ans)