h,w = map(int,input().split())
l = []
for i in range(h+1):
    if i == 0:
        l.append([0]*(w+1))
        continue
    l.append([0] + list(map(int,input().split())))
for i in range(len(l)):
    for j in range(1,w+1):
        l[i][j] += l[i][j-1]
for i in range(w+1):
    for j in range(1,h+1):
        l[j][i] += l[j-1][i]
ans = []
q = int(input())
for i in range(q):
    a,b,c,d = map(int,input().split())
    # ans.append(l[c][d]-l[a-1][b-1]) 二次元累積和の時は、単にこれをするだけではダメ。
    ans.append(l[c][d] - l[a-1][d] - l[c][b-1] + l[a-1][b-1])
# print(*l,sep="\n")
print(*ans,sep="\n")