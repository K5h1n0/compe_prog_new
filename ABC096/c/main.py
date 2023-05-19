h,w = map(int,input().split())
l = [list(input()) for _ in range(h)]
ans = "Yes"
for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            flg = 0
            for y,x in (-1,0),(0,1),(1,0),(0,-1):
                if 0 <= i + y < h and 0 <= j + x < w:
                    if l[i+y][j+x] == "#":
                        flg = 1
                        break
            if flg == 0:
                ans = "No"
                break
    else:
        continue
    break
print(ans)