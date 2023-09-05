n = int(input())
l = list(map(int, input().split()))
now = l[0]
ans = 1
for i in range(1, n):
    if l[i] <= now:
        ans += 1
        now = l[i]
print(ans)
