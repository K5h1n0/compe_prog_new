n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(input()))

judge = []
s = "###.*****"
s = list(s)
judge.append(s)
s = "###.*****"
s = list(s)
judge.append(s)
s = "###.*****"
s = list(s)
judge.append(s)
s = "....*****"
s = list(s)
judge.append(s)
s = "*********"
s = list(s)
judge.append(s)
s = "*****...."
s = list(s)
judge.append(s)
s = "*****.###"
s = list(s)
judge.append(s)
s = "*****.###"
s = list(s)
judge.append(s)
s = "*****.###"
s = list(s)
judge.append(s)

ans = []
for i in range(n-8):
    for j in range(m-8):
        if l[i][j] == judge[0][0]:
            flg = 1
            for k in range(9):
                for o in range(9):
                    
                    if judge[k][o] == "#" and l[i+k][j+o] == "#":
                        continue
                    elif judge[k][o] == "." and l[i+k][j+o] == ".":
                        continue
                    elif judge[k][o] == "*":
                        continue
                    else:
                        flg = 0
                        break
                else:
                    continue
                break
            if flg == 1:
                ans.append([i+1,j+1])
ans.sort()
for i in ans:
    print(*i)