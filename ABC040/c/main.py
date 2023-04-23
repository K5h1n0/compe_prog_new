n = int(input())
a = list(map(int,input().split()))
dp = [0]*len(a)
dp[1] = abs(a[1]-a[0])
for i in range(2,len(a)):
    tmp1 = dp[i-1] + abs(a[i] - a[i-1])
    tmp2 = dp[i-1] + abs(a[i] - a[i-2])
    dp[i] = min(tmp1,tmp2)
print(dp)

WA