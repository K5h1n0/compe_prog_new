# 分からん

from collections import deque

n,k = map(int,input().split())
p = list(map(int,input().split()))
l = sorted(p[:k],reverse=True)
now = l.pop()
big = deque(l)
small = set()
print(big)
print(now)
ans = [now]
for i in range(k+1,n):
    if now < p[i]:
        now = big.pop()
        ans.append(now)
        big.append(p[i])
        big = deque(sorted(big))
    else:
        ans.append(now)
print(*ans,sep="\n")