n = int(input())
l = list(map(int,input().split()))
ans = []
now = 0
for i in range(n*7):
    now += l[i]
    if i%7 == 6:
        ans.append(now)
        now = 0
print(*ans)