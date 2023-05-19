from collections import deque

n = int(input())
a = list(map(int,input().split()))
d = deque()
for i in range(len(a)):
    if i % 2== 0:
        d.append(a[i])
    else:
        d.appendleft(a[i])
if len(a) % 2 == 1:
    d.reverse()
print(*d)