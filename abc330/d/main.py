# 解説AC
n = int(input())
masu = []
x = []
for _ in range(n):
    inp = list(input())
    masu.append(inp)
    nowx = 0
    for i in inp:
        if i == "o":
            nowx += 1
    x.append(nowx)
y = []
for i in range(n):
    nowy = 0
    for j in range(n):
        if masu[j][i] == "o":
            nowy += 1
    y.append(nowy)
cnt = 0
for i in range(n):
    for j in range(n):
        if masu[i][j] == "o":
            cnt += (y[j]-1) * (x[i]-1)
print(cnt)