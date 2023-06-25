n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [0]*n
for i in range(1,n):
    if i == 1:
        dp[i] = a[i-1]
        continue
    dp[i] = min(dp[i-2] + b[i-2],dp[i-1]+a[i-1])
print(dp[-1])