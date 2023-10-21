"""
import heapq

n,a,b,c = map(int,input().split())
d = []
for i in range(n):
    inp = list(map(int,input().split()))
    d.append(inp)

def car(s):
    dist = [float("INF")]*n
    dist[s] = 0
    visited = [False]*n
    visited[s] = True
    q = []
    for v,cost in enumerate(d[s]):
        if visited[v]:
            continue
        heapq.heappush(q,(cost*a,v))
    while q:
        nowcost,nowv = heapq.heappop(q)
        if visited[nowv]:
            continue
        visited[nowv] = True
        dist[nowv] = nowcost
        for nextv,nextcost in enumerate(d[nowv]):
            if visited[nextv]:
                continue
            heapq.heappush(q,(nowcost+nextcost*a,nextv))
    return dist

def train(s):
    dist = [float("INF")]*n
    dist[s] = 0
    visited = [False]*n
    visited[s] = True
    q = []
    for v,cost in enumerate(d[s]):
        if visited[v]:
            continue
        heapq.heappush(q,(cost*b+c,v))
    while q:
        nowcost,nowv = heapq.heappop(q)
        if visited[nowv]:
            continue
        visited[nowv] = True
        dist[nowv] = nowcost
        for nextv,nextcost in enumerate(d[nowv]):
            if visited[nextv]:
                continue
            heapq.heappush(q,(nowcost+nextcost*b+c,nextv))
    return dist

fromstart = car(0)
fromgoal = train(n-1)
maximum = 10**15
for i in range(n):
    maximum = min(maximum,fromstart[i]+fromgoal[i])
print(maximum)
"""


import heapq

def dijkstra(n, d, a, b, c):
    def calculate_distances(s, multiplier, extra_cost=0):
        dist = [float("inf")] * n
        dist[s] = 0
        visited = [False] * n
        q = [(0, s)]

        while q:
            cost, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True
            dist[v] = cost

            for nextv, nextcost in enumerate(d[v]):
                if not visited[nextv]:
                    heapq.heappush(q, (cost + nextcost * multiplier + extra_cost, nextv))
        
        return dist

    fromstart = calculate_distances(0, a)
    fromgoal = calculate_distances(n - 1, b, c)

    minimum = float("inf")
    for i in range(n):
        minimum = min(minimum, fromstart[i] + fromgoal[i])

    return minimum

if __name__ == "__main__":
    n, a, b, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    
    result = dijkstra(n, d, a, b, c)
    print(result)