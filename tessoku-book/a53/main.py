#優先度付きキューの使いかた覚えるぞ～

import heapq

q = int(input())
l = []
ans = []
heapq.heapify(l)
for i in range(q):
    tmp = list(input().split())
    if tmp[0] == "1":
        heapq.heappush(l,int(tmp[1]))
    elif tmp[0] == "2":
        ans.append(min(l))
    elif tmp[0] == "3":
        heapq.heappop(l)
print(*ans,sep="\n")