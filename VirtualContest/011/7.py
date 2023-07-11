n = int(input())
l = []
maximum = 0
for _ in range(n):
    tmp = list(input())
    for i in tmp:
        maximum = max(maximum,int(i))
    l.append(tmp)
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
ans = 0
for i in  range(n):
    for j in range(n):
        if int(l[i][j]) == maximum:
            #処理開始
            now_list = []
            for k in range(8):
                now_num = ""
                for m in range(n):
                    now_num += l[(i+(dy[k])*m)%n][(j+(dx[k])*m)%n]
                now_list.append(int(now_num))
                # print(now_list)
            ans = max(ans,max(now_list))
print(ans)