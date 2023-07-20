#DP
x = int(input())
dp = [0]*100001
dp[100] = 1
dp[101] = 1
dp[102] = 1
dp[103] = 1
dp[104] = 1
dp[105] = 1
for i in range(1,100001):
    if dp[i] == 1:
        if i+100 < len(dp):
            dp[i+100] = 1
        if i+101 < len(dp):
            dp[i+101] = 1
        if i+102 < len(dp):
            dp[i+102] = 1
        if i+103 < len(dp):
            dp[i+103] = 1
        if i+104 < len(dp):
            dp[i+104] = 1
        if i+105 < len(dp):
            dp[i+105] = 1
print(dp[x])