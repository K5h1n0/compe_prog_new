n,q = map(int,input().split())
l = [0]*(n+1)
ans = []
for i in range(q):
    a,b = map(int,input().split())
    if a == 1:
        l[b] += 1
    elif a == 2:
        l[b] += 2
    elif a == 3:
        if l[b] >= 2:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans,sep="\n")