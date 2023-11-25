h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    skipflg = False
    for j in range(w-1):
        if skipflg:
            skipflg = False
            continue
        if s[i][j] == "T" and s[i][j+1] == "T":
            skipflg = True
            s[i][j] = "P"
            s[i][j+1] = "C"
for i in s:
    print(*i,sep="")