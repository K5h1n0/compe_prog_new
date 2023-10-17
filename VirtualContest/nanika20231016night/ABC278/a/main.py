from collections import deque

n,k = map(int,input().split())
a = list(map(int,input().split()))
d = deque(a)
for i in range(k):
    d.popleft()
    d.append(0)
print(*d)