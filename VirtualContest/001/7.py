n,m,x = map(int,input().split())
ans = 10**7
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(2**n):
    total = 0
    now = [0]*m
    for j in range(n):
        if ((i>>j) & 1):
            total += l[j][0]
            for k in range(m):
                now[k] += l[j][k+1]
    if x <= min(now) and total < ans:
        ans = total
if ans == 10**7:
    print(-1)
else:
    print(ans)