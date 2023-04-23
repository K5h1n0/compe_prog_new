from collections import defaultdict

n,q = map(int,input().split())
a = list(map(int,input().split()))
d = defaultdict(list)
for i in range(len(a)):
    d[a[i]].append(i+1)
ans = []
for i in range(q):
    x,k = map(int,input().split())
    if k-1 < len(d[x]):
        ans.append(d[x][k-1])
    else:
        ans.append(-1)
print(*ans,sep="\n")