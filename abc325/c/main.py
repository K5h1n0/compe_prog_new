from collections import deque

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
visited = [[0]*w for _ in range(h)]

x = [0,1,1,1,0,-1,-1,-1]
y = [-1,-1,0,1,1,1,0,-1]

ans = 0
for i in range(h):
    for j in range(w):
        if l[i][j] == "#" and visited[i][j] == 0:
            q = deque()
            visited[i][j] = 1
            q.append((i,j))
            while q:
                nowy,nowx = q.popleft()
                for k in range(8):
                    nexty = nowy + x[k]
                    nextx = nowx + y[k]
                    if 0 <= nexty < h and 0 <= nextx < w and l[nexty][nextx] == "#":
                        if visited[nexty][nextx] == 0:
                            visited[nexty][nextx] = 1
                            q.append((nexty,nextx))
            ans += 1                    
print(ans)