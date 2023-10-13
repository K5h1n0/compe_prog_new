n = int(input())
w = list(map(int,input().split()))
total = sum(w)
now = 0
ans = 999999999999
for i in range(len(w)-1):
    now += w[i]
    ans = min(ans,abs(now-(total-now)))
print(ans)