from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(pre,now):
    ans.append(now)
    for next in d[now]:
        if next == pre:
            continue
        dfs(now,next)
        ans.append(now)

n = int(input())
d = defaultdict(list)
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

for i,v in d.items(): #入力が必ずしも番号の小さい順に行われるとも限らないので、各節から出る枝を節の番号の昇順にソートする必要がある。
    d[i] = sorted(v)

ans = []
dfs(-1,1)
print(*ans)