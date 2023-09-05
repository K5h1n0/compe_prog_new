n = int(input())
a = list(map(int, input().split()))

a.reverse()
ans = 0
for i in range(n):
    ans += a[i]*2**i
print(ans)
