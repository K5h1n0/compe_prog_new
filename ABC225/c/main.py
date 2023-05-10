#ムズ
n,m = map(int,input().split())
b = []
for i in range(n):
    b.append(list(map(int,input().split())))
ans = "Yes"

r = (b[0][0] - 1 + 7)//7
c = (b[0][0] - 1)%7 + 1
for i in range(r,n+r):
    for j in range(c,m+c):
        if (i-r)*7+j != b[i-c][j-c]:
            ans = "No"
print(ans)