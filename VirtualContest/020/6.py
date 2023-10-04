n,m = map(int,input().split())
l = []
for i in range(m):
    c = int(input())
    l.append(set(list(map(int,input().split()))))

ans = 0
for i in range(2**m):
    nowset = set()
    for j in range(m):
        if((i>>j) & 1):
            nowset |= l[j]
    if len(nowset) == n:
        ans += 1
print(ans)
