n = int(input())
a = list(map(int,input().split()))
ans = a[:]
maxl = [0]*n
for i in range((n+1)//2):
    ans[i] = min(i+1,a[i])
    ans[-1-i] = min(i+1,a[-1-i])
now = 0
for i in range(n):
    now += 1
    if ans[i] < now:
        now = ans[i]
    ans[i] = min(now,ans[i])
now = 0
for i in range(n-1,-1,-1):
    now += 1
    if ans[i] < now:
        now = ans[i]
    ans[i] = min(now,ans[i])
print(max(ans))