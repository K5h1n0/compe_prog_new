from collections import deque

n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
d = deque(l)
for i in range(n):
    d.popleft()
    d.pop()
print(sum(d)/len(d))