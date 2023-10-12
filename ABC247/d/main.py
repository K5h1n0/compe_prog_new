from collections import deque

q = int(input())
queue = deque()
ans = []
for i in range(q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        queue.append([inp[1], inp[2]])
    elif inp[0] == 2:
        total = 0
        remain = inp[1]
        while 0 < remain:
            nowlist = queue.popleft()
            if remain < nowlist[1]:
                total += nowlist[0] * remain
                nowlist[1] -= remain
                remain = 0
                queue.appendleft(nowlist)
            elif remain >= nowlist[1]:
                total += nowlist[0] * nowlist[1]
                remain -= nowlist[1]
        ans.append(total)
print(*ans, sep="\n")
