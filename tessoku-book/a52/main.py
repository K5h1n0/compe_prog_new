from collections import deque

q = int(input())
ans = []
queue = deque()
for i in range(q):
    l = list(input().split())
    if l[0] == "1":
        queue.append(l[1])
    elif l[0] == "2":
        ans.append(queue[0])
    elif l[0] == "3":
        queue.popleft()
print(*ans,sep="\n")