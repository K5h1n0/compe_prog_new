n,m = map(int,input().split())
l = []
for i in range(m):
    c = int(input())
    l.append(list(map(int,input().split())))
ans = 0
for i in range(2**m):
    now = []
    for j in range(m):
        if (i>>j & 1):
            now += l[j]
    if len(set(now)) == n:
        ans += 1
print(ans)