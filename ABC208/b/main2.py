from math import factorial
import time

n = int(input())
coin = []
for i in range(1, 11):
    coin.append(factorial(i))
dp = [n]*(n+1)
dp[0] = 0
for c in coin:
    for i in range(c, n+1):
        dp[i] = min(dp[i], dp[i-c]+1)
        print(dp)
        time.sleep(0.01)

print(dp)
