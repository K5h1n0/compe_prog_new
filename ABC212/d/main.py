#解説AC 何でoffsetを引いてpushして、popしたものにoffsetを足すとうまくいくのか分からない。

import heapq

q = int(input())
queue = []
heapq.heapify(queue)
offset = 0
for i in range(q):
    now = list(map(int,input().split()))
    if now[0] == 1:
        heapq.heappush(queue,now[1]-offset)
    elif now[0] == 2:
        offset += now[1]
    elif now[0] == 3:
        print(heapq.heappop(queue)+offset)