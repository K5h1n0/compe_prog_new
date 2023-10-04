n,m = map(int,input().split())
ship1 = set()
ship2 = set()
for i in range(m):
    l = sorted(list(map(int,input().split())))
    if l[0] == 1:
        ship1.add(l[1])
    elif l[1] == n:
        ship2.add(l[0])

if ship1 & ship2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

"""
from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
flg = False

def dfs(now,cnt):
    global flg
    global n
    flg |= cnt == 0 and now == n
    if cnt <= 0:
        return
    for next in d[now]:
        dfs(next,cnt-1)
dfs(1,2)
if flg:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
"""