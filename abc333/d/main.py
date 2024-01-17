from collections import defaultdict,deque

n = int(input())
d = defaultdict(list)
for _ in range(n-1):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)
if len(d[1]) == 1:
    print(1)
    exit()

ans = []
for i in d[1]:
    q = deque()
    q.append(i)
    visited = [False]*(n+1)
    visited[i] = True
    now = 0
    while q:
        nowv = q.pop()
        if nowv == 1:
            continue
        for nextv in d[nowv]:
            if not visited[nextv]:
                visited[nextv] = True
                now += 1
                q.append(nextv)
    ans.append(now+1)
print(min(ans))