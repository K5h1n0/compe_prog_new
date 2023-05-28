n,m = map(int,input().split())
a = []
for i in range(m):
    a.append(list(map(int,input().split())))
l = []
for i in range(n):
    l.append([1]*n)
for i in range(m):
    for j in range(n-1):
        l[a[i][j]-1][a[i][j+1]-1] = 0
        l[a[i][j+1]-1][a[i][j]-1] = 0
ans = 0
for i in range(n):
    for j in range(n):
        ans += l[i][j]
print((ans-n)//2)