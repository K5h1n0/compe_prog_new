n = int(input())
masu = []
lx = []
combix = []
for i in range(n):
    inp = list(input())
    masu.append(inp)
    cnt = 0
    for j in range(n):
        if inp[j] == "o":
            cnt += 1
    lx.append(cnt)
    combix.append(cnt*(cnt-1)//2)
ly = []
combiy = []
for j in range(n):
    cnt = 0
    for i in range(n):
        if masu[i][j] == "o":
            cnt += 1
    ly.append(cnt)
    combiy.append(cnt*(cnt-1)//2)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if masu[i][k] == "o" and masu[j][k] == "o":
                ans += lx[i]-1
                ans += lx[j]-1
print(ans)