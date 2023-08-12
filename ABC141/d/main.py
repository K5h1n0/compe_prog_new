import heapq

n,m = map(int,input().split())
a = list(map(int,input().split()))
a = list(map(lambda n: n * -1, a))
heapq.heapify(a)
for i in range(m):
    now = heapq.heappop(a)
    now = now / 2
    now = int(now)
    heapq.heappush(a,now)
print(abs(sum(a)))