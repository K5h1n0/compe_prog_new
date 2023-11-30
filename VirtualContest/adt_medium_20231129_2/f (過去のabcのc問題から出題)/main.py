n = int(input())
l = []
for i in range(n):
    l.append(list(input()))

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

for i in range(n):
    for j in range(n):
        
        for k in range(8):
            nowcnt = 0
            for m in range(6):
                if 0 <= i+(dy[k]*m) < n and 0 <= j+(dx[k]*m) < n:
                    if l[i+(dy[k]*m)][j+(dx[k]*m)] == "#":
                        nowcnt += 1
                else:
                    break
            else:
                if 4 <= nowcnt:
                    print("Yes")
                    exit()
print("No")