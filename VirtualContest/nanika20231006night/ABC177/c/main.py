n = int(input())
a = list(map(int,input().split()))
accum = []
tmp = 0
for i in range(n-1,0,-1):
    tmp += a[i]
    accum.append(tmp)
accum.append(0)
accum.reverse()
ans = 0
for i in range(n-1):
    ans += a[i] * accum[i+1]
    ans %= 10**9+7
print(ans)