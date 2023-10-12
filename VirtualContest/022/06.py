from collections import deque,defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)
visited = [0]*n
ans = 0
for i in range(1,n+1):
    if visited[i-1] == 1:
        continue
    q = deque()
    q.append(i)
    visited[i-1] = 1
    while q:
        now = q.popleft()
        for next in d[now]:
            if visited[next-1] == 1:
                continue
            visited[next-1] = 1
            q.append(next)
    ans += 1
print(ans)