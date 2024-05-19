from collections import deque

h,w = map(int,input().split())
s = []
s2 = []
for i in range(h):
    inp = list(input())
    s.append(inp[:])
    s2.append(inp[:])
di = [-1,0,1,0]
dj = [0,1,0,-1]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            for k in range(4):
                nexti = i+di[k]
                nextj = j+dj[k]
                if 0 <= nexti < h and 0 <= nextj < w:
                    s2[nexti][nextj] = "#"

visited = [[False]*w for _ in range(h)]
maximum = 0
for i in range(h):
    for j in range(w):
        if s2[i][j] == ".":
            numset = set()
            visited[i][j] = True
            numset.add((i+1,j+1))
            d = deque()
            d.append((i,j))
            while d:
                nowi,nowj = d.popleft()
                for k in range(4):
                    nexti = nowi+di[k]
                    nextj = nowj+dj[k]
                    if 0 <= nexti < h and 0 <= nextj < w and not visited[nexti][nextj]:
                        numset.add((nexti,nextj))
                        if s2[nexti][nextj] == ".":
                            d.append((nexti,nextj))
                        visited[nexti][nextj] = True
            maximum = max(maximum, len(numset))
print(maximum+1)