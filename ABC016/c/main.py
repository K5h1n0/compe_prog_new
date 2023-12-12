from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

ans = [0]*n
for i in range(1,n+1):
    visited = [False]*(n+1)
    q = deque()
    q.append((i,0))
    visited[i] = True
    while q:
        nowv,nowcnt = q.popleft()
        if nowcnt == 2:
            ans[i-1] += 1
            continue
        for nextv in d[nowv]:
            if not visited[nextv]:
                visited[nextv] = True
                q.append((nextv,nowcnt+1))
print(*ans,sep="\n")