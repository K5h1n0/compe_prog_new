q = int(input())
a = []
ans = []
for i in range(q):
    x,y = map(int,input().split())
    if x == 1:
        a.append(y)
    elif x == 2:
        ans.append(a[-y])
print(*ans,sep="\n")