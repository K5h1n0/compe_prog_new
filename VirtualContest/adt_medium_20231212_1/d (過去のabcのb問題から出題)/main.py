from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(1,n):
    for j in range(i+1,n+1):
        d[(i,j)] = 0
for i in range(m):
    inp = list(map(int,input().split()))
    for j in range(1,n):
        a = inp[j-1]
        b = inp[j]
        if b < a:
            a,b = b,a
        d[(a,b)] += 1
ans = 0
for i in d.values():
    if i == 0:
        ans += 1
print(ans)