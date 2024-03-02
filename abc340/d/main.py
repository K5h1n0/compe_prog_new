from collections import defaultdict
import heapq

n = int(input())
d = defaultdict(list)
for i in range(n-1):
    a,b,x = map(int,input().split())
    d[i].append((a,i+1))
    d[i].append((b,x-1))

ans = [float('inf')]*n
visited = [False]*n

q = []
heapq.heapify(q)
#開始地点には0で到着できる
ans[0] = 0
for next in d[0]:
    #開始地点から進める場所をheapqに入れる。
    heapq.heappush(q,next)
while q:
    nowcost,nowv = heapq.heappop(q)
    if visited[nowv]:
        continue
    visited[nowv] = True
    ans[nowv] = nowcost
    for nextcost,nextv in d[nowv]:
        if visited[nextv]:
            continue
        heapq.heappush(q,(nowcost+nextcost,nextv))
print(ans[-1])