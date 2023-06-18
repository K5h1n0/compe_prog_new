n,k,q = map(int,input().split())
l = []
a = [0]*n
ans = []
for i in range(q):
    x,y = map(int,input().split())
    a[x-1] = y
    ans.append(a[:])
print(*ans,sep="\n")