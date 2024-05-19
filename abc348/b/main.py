n = int(input())
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
ans = []
for i in range(n):
    nowx,nowy = l[i][0],l[i][1]
    now = []
    maximum = 0
    for j in range(n):
        dist = ((nowx-l[j][0])**2 + (nowy-l[j][1])**2)**0.5
        maximum = max(maximum,dist)
        now.append(dist)
    for j in range(n):
        if now[j] == maximum:
            ans.append(j+1)
            break
print(*ans,sep="\n")