from collections import deque
import time 

n,m = map(int,input().split())
field = []
touched = []
direction = []
for i in range(n):
    field.append(input())
    touched.append([0]*m)
    direction.append([0]*m)
q = deque()

touched[1][1] = 1
direction[1][1] = 16
for i in range(n):
    for j in range(m):
        if direction[i][j] != 0:
            q.append((i,j))
            while q:
                nowi,nowj = q.popleft()
                if field[nowi][nowj+1] == "." and direction[nowi][nowj] & 1 == 0:
                    touched[nowi][nowj+1] = 1
                    direction[nowi][nowj] += 1
                    for k in range(m):
                        if nowj+1+k < m and field[nowi][nowj+1+k] == ".":
                            touched[nowi][nowj+1+k] = 1

                        elif nowj+1+k < m and field[nowi][nowj+1+k] == "#":
                            q.append((nowi,nowj+k))
                            break
                
                if field[nowi+1][nowj] == "." and direction[nowi][nowj] & 2 == 0:
                    direction[nowi][nowj] += 2
                    touched[nowi+1][nowj] = 1
                    for k in range(n):
                        if nowi+1+k < n and field[nowi+1+k][nowj] == ".":
                            touched[nowi+1+k][nowj] = 1

                        elif nowi+1+k < n and field[nowi+1+k][nowj] == "#":
                            q.append((nowi+k,nowj))
                            break
                
                if field[nowi][nowj-1] == "." and direction[nowi][nowj] & 4 == 0:
                    direction[nowi][nowj] += 4
                    touched[nowi][nowj-1] = 1
                    for k in range(m):
                        if nowj-1-k < m and field[nowi][nowj-1-k] == ".":
                            touched[nowi][nowj-1-k] = 1

                        elif nowj-1-k < m and field[nowi][nowj-1-k] == "#":
                            q.append((nowi,nowj-k))
                            break
                
                if field[nowi-1][nowj] == "." and direction[nowi][nowj] & 8 == 0:
                    direction[nowi][nowj] += 8
                    touched[nowi-1][nowj] = 1
                    for k in range(n):
                        if nowi-1-k < n and field[nowi-1-k][nowj] == ".":
                            touched[nowi-1-k][nowj] = 1

                        elif nowi-1-k < n and field[nowi-1-k][nowj] == "#":
                            q.append((nowi-k,nowj))
                            break

ans = 0
for i in range(n):
    ans += sum(touched[i])
print(ans)