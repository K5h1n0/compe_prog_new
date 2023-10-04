n,x = map(int,input().split())
a = list(map(int,input().split()))
ans = []
for i in range(0,101):
    l = a[:] + [i]
    total = sum(l) - min(l) - max(l)
    if x <= total:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))