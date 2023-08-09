import heapq

n,k = map(int,input().split())
p = list(map(int,input().split()))
q = p[0:k]
#print(q)
heapq.heapify(q) #元々あるリストをヒープ化

for i in range(k,n):
    now = heapq.heappop(q)
    print(now)
    #print(q)
    #print(i,p[i])
    if now < p[i]:
        heapq.heappush(q,p[i])
    else:
        heapq.heappush(q,now)
print(heapq.heappop(q))


"""
# 解説AC
import heapq

n,k = map(int,input().split())
p = list(map(int,input().split()))
q = p[0:k]
print(min(q))
heapq.heapify(q)
for i in range(k,n):
    minimum = heapq.heappop(q)
    minimum = max(minimum,p[i])
    heapq.heappush(q,minimum)
    ans = heapq.heappop(q)
    print(ans)
    heapq.heappush(q,ans)
"""
