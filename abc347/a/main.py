n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = []
for i in range(n):
    if l[i] % k == 0:
        ans.append(l[i]//k)
print(*ans)