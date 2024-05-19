from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

ans = 0
visited = [False]*(n+1)
for i in range(1,n+1):
    if visited[i]:
        continue
    visited[i] = True
    cnt = 1
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        for next in d[now]:
            if visited[next]:
                continue
            visited[next] = True
            cnt += 1
            q.append(next)
    ans += (cnt*(cnt-1))//2
print(ans-m)