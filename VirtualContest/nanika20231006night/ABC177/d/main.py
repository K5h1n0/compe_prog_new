from collections import defaultdict,deque

n, m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
visited = [0]*(n+1)
maximum = 0
for i in range(1,n+1):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    visited[i] = 1
    nowtotal = 1
    while q:
        now = q.popleft()
        for next in d[now]:
            if visited[next] == 0:
                visited[next] = 1
                nowtotal += 1
                q.append(next)
    maximum = max(maximum,nowtotal)
print(maximum)