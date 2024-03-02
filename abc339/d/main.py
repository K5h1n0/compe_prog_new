from collections import deque

n = int(input())
s = [list(input()) for _ in range(n)]
p1i,p1j,p2i,p2j = 0,0,0,0
flg = False
for i in range(n):
    for j in range(n):
        if s[i][j] == "P":
            if not flg:
                p1i = i
                p1j = j
                flg = True
            else:
                p2i = i
                p2j = j
                break
    else:
        continue
    break

visited = [[[[False]*n for _ in range(n)] for _ in range(n)]for _ in range(n)]

di = [-1,0,1,0]
dj = [0,1,0,-1]

q = deque()
nowstate = (p1i,p1j,p2i,p2j)
q.append((nowstate,0))
while q:
    nowstate,nowcnt = q.popleft()
    nowp1i,nowp1j,nowp2i,nowp2j = nowstate
    if nowp1i == nowp2i and nowp1j == nowp2j:
        print(nowcnt)
        exit()
    for i in range(4):
        nextp1i = nowp1i + di[i]
        nextp1j = nowp1j + dj[i]
        nextp2i = nowp2i + di[i]
        nextp2j = nowp2j + dj[i]
        if not (0 <= nextp1i < n and 0 <= nextp1j < n and s[nextp1i][nextp1j] != "#"):
            nextp1i = nowp1i
            nextp1j = nowp1j
        if not (0 <= nextp2i < n and 0 <= nextp2j < n and s[nextp2i][nextp2j] != "#"):
            nextp2i = nowp2i
            nextp2j = nowp2j
        nextstate = (nextp1i,nextp1j,nextp2i,nextp2j)
        if not visited[nextp1i][nextp1j][nextp2i][nextp2j]:
            visited[nextp1i][nextp1j][nextp2i][nextp2j] = True
            q.append((nextstate,nowcnt+1))
print(-1)