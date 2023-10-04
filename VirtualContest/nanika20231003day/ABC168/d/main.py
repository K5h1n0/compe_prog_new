from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
l = [-1]*n
visited = [False]*n


def dfs(pre, now):
    global l
    l[now] = pre
    for next in d[now]:
        dfs(now, next)


print(l)
