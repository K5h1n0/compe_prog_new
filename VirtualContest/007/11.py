n = int(input())
l = []
for i in range(n):
    l.append(list(input()))
ans = 0
for j in range(9):
    flg = 0
    for i in range(n):
        if flg == 0:
            if l[i][j] == "o":
                flg = 1
        elif flg == 1:
            if l[i][j] != "o":
                flg = 0
                ans += 1
        if l[i][j] == "x":
            ans += 1
    if flg == 1:
        ans += 1
print(ans)