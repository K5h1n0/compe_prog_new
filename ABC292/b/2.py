n,q = map(int,input().split())
l = [0] * n
ans = []
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        l[query[1]-1] += 1
    elif query[0] == 2:
        l[query[1]-1] += 2
    elif query[0] == 3:
        if l[query[1]-1] >= 2:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans,sep="\n")