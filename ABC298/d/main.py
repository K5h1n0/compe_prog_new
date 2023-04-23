from collections import deque

q = int(input())
queue = deque()
queue.append("1")
i = 0
j = 0
now = "1"
for __ in range(q):
    tmp = list(input().split())
    if tmp[0] == "1":
        queue.append(tmp[1])
    elif tmp[0] == "2":
        queue.popleft()
    elif tmp[0] == "3":
        print(now)
    now = int("".join(queue))%998244353