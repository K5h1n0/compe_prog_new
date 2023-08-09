"""
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[-1]*n for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = b[0]
for i in range(1,n):
    if dp[0][i-1] != -1 and abs(dp[0][i-1] - a[i]) <= k:
        dp[0][i] = a[i]
    if dp[0][i-1] != -1 and abs(dp[0][i-1] - b[i]) <= k:
        dp[1][i] = b[i]
    if dp[1][i-1] != -1 and abs(dp[1][i-1] - a[i]) <= k:
        dp[0][i] = a[i]
    if dp[1][i-1] != -1 and abs(dp[1][i-1] - b[i]) <= k:
        dp[1][i] = b[i]
    if dp[0][i] == -1 and dp[1][i] == -1:
        print("No")
        exit()
if dp[0][-1] != -1 or dp[1][-1] != -1:
    print("Yes")
else:
    print("No")
"""
# 解説を見て書いた。同じくDPだが0と1で判断した。
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1
for i in range(1,n):
    if dp[0][i-1]:
        if abs(a[i-1] - a[i]) <= k:
            dp[0][i] = 1
        if abs(a[i-1] - b[i]) <= k:
            dp[1][i] = 1
    if dp[1][i-1]:
        if abs(b[i-1] - a[i]) <= k:
            dp[0][i] = 1
        if abs(b[i-1] - b[i]) <= k:
            dp[1][i] = 1
if dp[0][-1] or dp[1][-1]:
    print("Yes")
else:
    print("No")