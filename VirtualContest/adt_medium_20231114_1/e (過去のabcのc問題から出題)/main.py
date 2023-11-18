import sys
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())
l = []
for _ in range(h):
    l.append(list(input()))
visited = [[False]*w for _ in range(h)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

nowi = 0
nowj = 0

def dfs(i,j):
    global nowi,nowj
    if visited[i][j] == True:
        return -1
    visited[i][j] = True
    if l[i][j] == "U":
        tmp = 0
    elif l[i][j] == "D":
        tmp = 1
    elif l[i][j] == "L":
        tmp = 2
    elif l[i][j] == "R":
        tmp = 3
    nexti = i + di[tmp]
    nextj = j + dj[tmp]
    nowi = i
    nowj = j
    if 0 <= nexti < h and 0 <= nextj < w:
        return dfs(nexti,nextj)

if dfs(0,0) == -1:
    print(-1)
else:
    print(nowi+1,nowj+1)