n = int(input())
l = list(map(int,input().split()))
ans = []
for i in range(n):
    if l[i] % 2 == 0:
        ans.append(l[i])
print(*ans)