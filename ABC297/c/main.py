h,w = map(int,input().split())
l = []
for i in range(h):
    tmp = list(input())
    l.append(tmp)
for i in range(h):
    flg = 0
    for j in range(w-1):
        if flg == 1:
            flg = 0
            continue
        if l[i][j] == "T" and l[i][j+1] == "T":
            l[i][j] = "P"
            l[i][j+1] = "C"
            flg = 1
for i in range(len(l)):
    print(*l[i],sep="")