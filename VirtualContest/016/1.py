n = int(input())
l = [0] + list(map(int, input().split()))
ans = []
for i in range(1, n+1):
    ans.append(l[i]-l[i-1])
print(*ans)
