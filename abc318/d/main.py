from collections import defaultdict, deque

n = int(input())
d = defaultdict(list)
for i in range(1, n):
    l = list(map(int, input().split()))
    now = 1
    for j in range(i+1, n+1):
        d[i].append((j, l[now-1]))
        d[j].append((i, l[now-1]))
        now += 1
print(d)

s = set()
max = 0


def dfs(now, flg, visited):
    global max
    if visited[now-1] == 1:
        return
    print(now, s)
    visited[now-1] = 1
    if flg == 0:
        s.add(now)
    for next in d[now]:
        flg ^= 1
        dfs(next[0], flg, visited)


dfs(1, 0, [0]*n)
print()
