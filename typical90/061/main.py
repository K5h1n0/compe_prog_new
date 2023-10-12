from collections import deque

q = int(input())
ans = []
queue = deque()
for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        queue.appendleft(x)
    elif t == 2:
        queue.append(x)
    elif t == 3:
        ans.append(queue[x-1])
print(*ans,sep="\n")