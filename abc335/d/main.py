import sys
sys.setrecursionlimit(10**6)

n = int(input())
l = [[""]*n for _ in range(n)]
l[n//2][n//2] = "T"

def f(nowi,nowj,direct,nowcnt):
    global l
    l[nowi][nowj] = str(nowcnt)
    nexti = nowi
    nextj = nowj
    if direct == 0:
        nextj += 1
    elif direct == 1:
        nexti += 1
    elif direct == 2:
        nextj -= 1
    elif direct == 3:
        nexti -= 1
    if 0 <= nexti < n and 0 <= nextj < n:
        if l[nexti][nextj] == "":
            f(nexti,nextj,direct,nowcnt+1)
        elif l[nexti][nextj] == "T":
            return
        else:
            direct = (direct + 1)%4
            f(nowi,nowj,direct,nowcnt)
    else:
        direct = (direct + 1)%4
        f(nowi,nowj,direct,nowcnt)
f(0,0,0,1)
for i in l:
    print(*i)