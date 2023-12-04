from collections import defaultdict,deque

n,m = map(int,input().split())
c = list(map(int,input().split()))
cd = defaultdict(int)
for i in list(set(c)):
    cd[i] = 0
c = [0] + c
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
for i in range(1,n+1):
    if visited[i]:
        continue
    q = deque()
    nowcolor = c[i]
    q.append(i)
    visited[i] = True
    while q:
        nowv = q.popleft()
        for nextv in d[nowv]:
            if c[nextv] == nowcolor and visited[nextv] == False:
                visited[nextv] = True
                q.append(nextv)
    cd[nowcolor] += 1
ans = 0
for i in cd.values():
    ans += i-1
print(ans)