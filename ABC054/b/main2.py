n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(input()))
b = []
for _ in range(m):
    b.append(list(input()))
for i in range(n-m+1):
    for j in range(n-m+1):
        flg = True
        for k in range(m):
            for o in range(m):
                flg &= a[i+k][j+o] == b[k][o]
        if flg:
            print("Yes")
            exit()
print("No")