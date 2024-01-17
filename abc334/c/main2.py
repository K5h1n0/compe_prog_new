n,k = map(int,input().split())
a = list(map(int,input().split()))

if k%2 and 1 < k:
    l1 = []
    for i in range(k-1,0,-1):
        l1.append(a[i] - a[i-1])
    l1.reverse()
    l2 = []
    for i in range(len(l1)-1):
        l2.append(l1[i]+l1[i+1])
    maxl2 = max(l2)
    maxl2index = l2.index(maxl2)
    del a[maxl2index+1]
elif k%2 and k == 1:
    del a[0]

aset = set(a[:])
l = []
for i in range(1,n+1):
    l.append(i)
    if i not in aset:
        l.append(i)

ans = 0
for i in range(0,len(l),2):
    ans += abs(l[i]-l[i+1])
print(ans)