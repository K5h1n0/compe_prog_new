h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(input()))
flg_lst_h = [False] * h
flg_lst_w = [False] * w
for i in range(h):
    for j in range(w):
        flg_lst_h[i] |= a[i][j] == "#"
for i in range(w):
    for j in range(h):
        flg_lst_w[i] |= a[j][i] == "#"
ans = []
xindex = -1
for i in range(h):
    if flg_lst_h[i]:
        ans.append([])
        xindex += 1
    else:
        continue
    for j in range(w):
        if flg_lst_w[j]:
            ans[xindex].append(a[i][j])
for i in ans:
    print(*i,sep="")