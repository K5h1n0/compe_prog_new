import sys
sys.setrecursionlimit(10**6)

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
            if nowy+1 == h:
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy+1,nowx)
        elif l[nowy][nowx] == "L":
            if nowx == 0:
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy,nowx-1)
        elif l[nowy][nowx] == "R":
            if nowx+1 == w:
                print(nowy+1,nowx+1)
                exit()
            dfs(nowy,nowx+1)

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
searched = [[0 for __ in range(w)] for __ in range(h)]

dfs(0,0)