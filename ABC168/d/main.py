from collections import defaultdict, deque

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

visited = [0]*(n+1)
q = deque()
q.append((1, 10**10))
while q:
    now, pre = q.popleft()
    if visited[now] == 0:
        visited[now] = pre
    else:
        continue
    for next in d[now]:
        if visited[next] == 0:
            q.append((next, now))
print("Yes")
for i in range(2, len(visited)):
    print(visited[i])
