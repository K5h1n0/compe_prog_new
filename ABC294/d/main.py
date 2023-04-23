import heapq

n,q = map(int,input().split())
ans = []
not_call = list(range(1,n+1))
heapq.heapify(not_call)
called1 = []
heapq.heapify(called1)
called2 = set()
called3 = set()
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        heapq.heappush(called1,heapq.heappop(not_call))
    elif query[0] == 2:
        x = query[1]
        called3.add(x)
    elif query[0] == 3:
        for j in range(len(called1)):
            if called1[j] in called3:
                pass
            else:
                ans.append(called1[j])
                break
print(*ans,sep="\n")