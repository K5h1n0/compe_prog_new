from collections import defaultdict

n = int(input())
b = list(map(int,input().split()))
a = sorted(b[:],reverse=True)
d = defaultdict(int)
now = a[0]
d[a[0]] = 0
nowtotal = 0
for i in range(len(a)):
    if now == a[i]:
        nowtotal += a[i]
    else:
        now = a[i]
        d[a[i]] = nowtotal
        nowtotal += a[i]
ans = []
for i in range(len(a)):
    ans.append(d[b[i]])
print(*ans)