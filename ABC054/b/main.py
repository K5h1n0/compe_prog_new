n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(input()))
b = []
for i in range(m):
    b.append(list(input()))
flg = False
for i in range(n-m+1):
    for j in range(n-m+1):
        flg2 = True
        for k in range(m):
            for l in range(m):
                flg2 &= a[i+k][j+l] == b[k][l]
        if flg2:
            flg = True
print("Yes" if flg else "No")
