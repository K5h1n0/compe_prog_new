from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
q = deque()
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

#方針
#まず、連結成分の個数を求めたい
#それぞれの連結成分に点が何個ずつあるか求める
#頂点の数-1が、その連結成分で残さないと連結構造が壊れてしまう辺の数
#この残さないといけない辺を全部の連結成分で調べて、数を足し合わせていく
#辺の数m-その足し合わせた数=消せる辺の数

total = 0
l = [0]*(n+1)
#全部の頂点から調べる必要がある
for i in range(1,n+1):
    if l[i] == 1:
        continue    
    cnt = 1 #忘れがち
    l[i] = 1 #忘れがち
    q.append(i)
    while q:
        tmp = q.popleft()
        for j in d[tmp]:
            if l[j] == 0:
                l[j] = 1
                cnt += 1
                q.append(j)
    total += cnt-1
ans = m - total
print(ans)