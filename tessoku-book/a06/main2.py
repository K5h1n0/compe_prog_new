n,q = map(int,input().split())
a = [0] + list(map(int,input().split()))
ans = []
for i in range(1,len(a)):
    a[i] += a[i-1]
for i in range(q):
    left,right = map(int,input().split())
    ans.append(a[right]-a[left-1])
print(*ans,sep="\n")