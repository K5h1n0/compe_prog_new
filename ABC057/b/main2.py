n,m = map(int,input().split())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
cp = []
for _ in range(m):
    c,d = map(int,input().split())
    cp.append([c,d])
ans = []
for i in range(n):
    x1 = l[i][0]
    y1 = l[i][1]
    min = 10**10
    for j in range(m):
        x2 = cp[j][0]
        y2 = cp[j][1]
        now = abs(x1-x2) + abs(y1-y2)
        if now < min:
            min = now
            idx = j + 1
    ans.append(idx)
print(*ans,sep="\n")