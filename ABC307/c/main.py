ha,wa = map(int,input().split())
la = []
for i in range(ha):
    la.append(list(input()))
hb,wb = map(int,input().split())
lb = []
for i in range(hb):
    lb.append(list(input()))
hx,wx = map(int,input().split())
lx = []
flg = 0
minkurox = 1000
maxkurox = 0
for i in range(hx):
    inp = list(input())
    if "#" in inp:
        if flg == 0:
            minkuroy = i
            flg = 1
        maxkuroy = i
        for j in range(len(inp)):
            if inp[j] == "#":
                minkurox = min(minkurox,j)
                maxkurox = max(maxkurox,j)
    lx.append(inp)
print(*lx,sep="\n")
ans = "No"

