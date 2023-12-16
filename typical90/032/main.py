import itertools

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
l = set()
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    l.add((x,y))
ans = []
for p in itertools.permutations(range(n)):
    flg = True
    now = 0
    for i in range(len(p)):
        now += a[p[i]][i]
        if i < len(p)-1 and tuple(sorted([p[i],p[i+1]]))in l:
            flg = False
            break
    if flg:
        ans.append(now)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))