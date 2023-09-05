n, x = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
dp = [[0]*(x+1) for _ in range(n)]
a = l[0][0]
b = l[0][1]
if a < x+1:
    dp[0][a] = 1
if b < x+1:
    dp[0][b] = 1
for i in range(1, n):
    a = l[i][0]
    b = l[i][1]
    for j in range(x+1):
        if dp[i-1][j] == 1:
            if j+a < x+1:
                dp[i][j+a] = 1
            if j+b < x+1:
                dp[i][j+b] = 1
print("Yes" if dp[-1][-1] else "No")
