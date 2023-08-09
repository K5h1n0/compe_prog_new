#動的計画法なのか……？
n = int(input())
p = list(map(int,input().split()))
dp = [0]*200001
ans = []
now = 0
for i in range(len(p)):
    dp[p[i]] = 1
    while dp[now] == 1:
        now += 1
    ans.append(now)
print(*ans,sep="\n")
