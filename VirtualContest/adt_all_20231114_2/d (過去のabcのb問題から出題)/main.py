from collections import deque

s = input()
q = deque(list(s))
l = []
for i in range(len(s)):
    now = q.popleft()
    q.append(now)
    l.append("".join(q))
l.sort()
print(l[0])
print(l[-1])