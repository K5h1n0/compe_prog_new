from collections import deque,defaultdict

n = int(input())
d = defaultdict(list)
time = [0]
for i in range(1,n+1):
    t,k,*a = map(int,input().split())
    time.append(t)
    d[i] = a
ans = time[n]
visited = [False]*(n+1)
visited[n] = True
q = deque()
for i in d[n]:
    q.append(i)
while q:
    nowv = q.popleft()
    ans += time[nowv]
    for nextv in d[nowv]:
        if not visited[nextv]:
            q.append(nextv)
            visited[nextv] = True
print(ans)