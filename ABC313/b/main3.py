from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for __ in range(m):
    a,b = map(int,input().split())
    d[a].append(b) #強い方から弱い方に辺を張る

ans = -1
for i in range(1,n+1):
    q = deque()
    bo = [0]*n
    q.append(i)
    bo[i-1] = 1
    while q:
        now = q.popleft()
        for next in d[now]:
            if bo[next-1] == 0:
                bo[next-1] = 1
                q.append(next)
    if sum(bo) == n: #全ての点からBFSを行なって、全ての点を訪問する回があれば、始点の人が最強である。
        ans = i
        break
print(ans)