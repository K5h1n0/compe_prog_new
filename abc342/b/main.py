n = int(input())
p = list(map(int,input().split()))
q = int(input())
ans = []
for i in range(q):
    a,b = map(int,input().split())
    for j in range(len(p)):
        if a == p[j]:
            ans.append(a)
            break
        elif b == p[j]:
            ans.append(b)
            break
print(*ans,sep="\n")