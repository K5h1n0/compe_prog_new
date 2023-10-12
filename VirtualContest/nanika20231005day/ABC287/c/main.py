from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
l = [0]*(n+1)
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)
    l[u] += 1
    l[v] += 1
l.sort()
if not(l[1] == 1 and l[2] == 1 and max(l) <= 2):
    print("No")
    exit()
visited = [0]*(n+1)
q = deque()
q.append(1)
while q:
    now = q.popleft()
    for next in d[now]:
        if visited[next] == 0:
            visited[next] = 1
            q.append(next)
if sum(visited[1:]) == n:
    print("Yes")
else:
    print("No")