a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
s = set()
for i in range(n):
    s.add(int(input()))
l = [[False]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        l[i][j] = a[i][j] in s
ansflg = False
for i in range(3):
    flg = True
    for j in range(3):
        flg &= l[i][j]
    ansflg |= flg
    flg = True
    for j in range(3):
        flg &= l[j][i]
    ansflg |= flg
ansflg |= l[0][0] and l[1][1] and l[2][2]
ansflg |= l[2][0] and l[1][1] and l[0][2]
print("Yes" if ansflg else "No")