h,w = map(int,input().split())
s = []
for i in range(h):
    inp = list(input())
    s.append(inp)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for i in range(h):
    for j in range(w):
        
        if s[i][j] != ".":
            continue
        cnt = 0
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < h and 0 <= x < w:
                if s[y][x] == "#":
                    cnt += 1
        if 2 <= cnt:
            print(i+1,j+1)
            exit()