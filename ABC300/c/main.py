h,w = map(int,input().split())
x = [
    ["#",".","#"],
    [".","#","."],
    ["#",".","#"],
    ]
l = []
for i in range(h):
    l.append(list(input()))
ans = [0]*min(h,w)
for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            flg = 1

            for k in range(3):
                for m in range(3):
                    if i+k <= h-1 and j+m <= w-1: 
                        if l[i+k][j+m] != x[k][m]:
                            flg = 0
                            break
                    else:
                        flg = 0
                        break
                else:
                    continue
                break
            if flg == 1:
                x_len = 0
                for n in range(3,len(ans)+1):
                    nowy = i+n
                    nowx = j+n
                    if nowy <= h-1 and nowx <= w-1:
                        if l[nowy][nowx] == "#":
                            x_len += 1
                            continue
                        else:
                            ans[x_len] += 1
                            break
                    else:
                        ans[x_len] += 1
                        break
print(*ans)