n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(len(a)-1,-1,-1):
    ans += (2**i)*a[n-1-i]
print(ans)