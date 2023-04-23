from collections import deque

n = int(input())
l = list(map(int,input().split()))
l.sort()
cnt = 0
i = 0
while i < len(l):
    if i + 1 < len(l) and l[i] == l[i+1]:
        cnt += 1
        i += 2
    else:
        i += 1
print(cnt)