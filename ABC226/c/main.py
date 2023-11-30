from collections import defaultdict,deque

n = int(input())
d = defaultdict(list)
t = [0]
for i in range(1,n+1):
    nowt,k,*alist = map(int,input().split())
    t.append(nowt)
    d[i] = alist

visited = [False]*(n+1)
q = deque()
q.append(n)
visited[n] = True
while q:
    now = q.popleft()
    for next in d[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)

ans = 0
for i in range(1,n+1):
    if visited[i]:
        ans += t[i]
print(ans)