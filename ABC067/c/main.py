n = int(input())
a = list(map(int,input().split()))
l = []
tmp = 0
for i in range(n):
    tmp += a[i]
    l.append(tmp)
ans = 10**10
for i in range(len(l)-1):
    ans = min(ans,abs(l[i] - (l[-1]-l[i])))
print(ans)