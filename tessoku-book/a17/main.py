#解説AC
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [0]*n
for i in range(1,n):
    if i == 1:
        dp[i] = a[i-1]
    dp[i] = min(dp[i-1]+a[i-1],dp[i-2]+b[i-2])
int_answer = dp[-1]
ans = []
index = n-1
while True:
    # こんなシュッとした処理が書けるようになりたい……。
    ans.append(index+1)
    if index == 0:
        break
    if dp[index-1]+a[index-1] == dp[index]:
        index -= 1
    else:
        index -= 2
ans.reverse()
print(len(ans))
print(*ans)