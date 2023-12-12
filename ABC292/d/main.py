from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)

flg = True
visited = [False]*(n+1)
for i in range(1,n+1):
    if visited[i]:
        continue
    visited[i] = True
    q = deque()
    q.append(i)
    sidecnt = 0
    vcnt = 0
    vcnt += 1
    while q:
        nowv = q.popleft()
        for nextv in d[nowv]:
            sidecnt += 1
            if visited[nextv]:
                continue
            vcnt += 1
            visited[nextv] = True
            q.append(nextv)
    flg &= sidecnt//2 == vcnt
print("Yes" if flg else "No")