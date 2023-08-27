n, w = map(int, input().split())
l = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(n+1):
    if i == 0:
        continue
    for j in range(w+1):
        weight = l[i][0]
        value = l[i][1]
        if j - weight < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
print(dp[n][w])
