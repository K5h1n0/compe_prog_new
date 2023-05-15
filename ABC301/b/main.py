n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n-1):
    if abs(a[i] - a[i+1]) == 1:
        ans += [a[i]]
        continue
    ans += [a[i]]
    tmp = list(range(min(a[i],a[i+1])+1,max(a[i],a[i+1])))
    if a[i] > a[i+1]:
        tmp.reverse()
    ans += tmp
ans += [a[-1]]
print(*ans)