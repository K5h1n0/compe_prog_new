n,d = map(int,input().split())
l = []
for i in range(n):
    l.append(list(input()))
date = [0]*d
for i in range(d):
    flg = 1
    for j in range(n):
        if l[j][i] == "x":
            flg = 0
    if flg == 1:
        date[i] = 1
tmp = 0
ans = 0
for i in range(len(date)):
    if date[i] == 1:
        tmp += 1
    else:
        tmp = 0
    ans = max(tmp,ans)
print(ans)