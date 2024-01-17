from collections import deque

r,c = map(int,input().split())
b = []
b2 = []
for i in range(r):
    tmp = list(input())
    b.append(tmp[:])
    b2.append(tmp[:])

dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(r):
    for j in range(c):
        if ord("1") <= ord(b[i][j]) <= ord("9"):
            q = deque()
            q.append((i,j,int(b[i][j])))
            visited = [[False]*c for _ in range(r)]
            visited[i][j] = True
            while q:
                nowi,nowj,nowcnt = q.popleft()
                b2[nowi][nowj] = "."
                for k in range(4):
                    nexti = nowi + dy[k]
                    nextj = nowj + dx[k]
                    nextcnt = nowcnt - 1
                    if 0 <= nexti < r and 0 <= nextj < c and visited[nexti][nextj] == False and 0 <= nextcnt:
                        q.append((nexti,nextj,nextcnt))
                        visited[nexti][nextj] = True
for i in b2:
    print(*i,sep="")