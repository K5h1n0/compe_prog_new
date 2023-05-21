import sys
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
searched = [[0 for __ in range(w)]for __ in range(h)]

def dfs(nowy,nowx):
    if searched[nowy][nowx] == 1:
        print(-1)
        exit()
    else:
        searched[nowy][nowx] = 1
        if l[nowy][nowx] == "U":
            if nowy == 0:
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy-1,nowx)
        elif l[nowy][nowx] == "D":
            if nowy == h-1: #ここの-1入れるの忘れて悩んだ
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy+1,nowx)
        elif l[nowy][nowx] == "L":
            if nowx == 0:
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy,nowx-1)
        elif l[nowy][nowx] == "R":
            if nowx == w-1: #ここの-1入れるの忘れて悩んだ
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy,nowx+1)

dfs(0,0)