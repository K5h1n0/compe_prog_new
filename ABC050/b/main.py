n = int(input())
t = list(map(int, input().split()))
total = sum(t)
m = int(input())
ans = []
for _ in range(m):
    p, x = map(int, input().split())
    ans.append(total-t[p-1]+x)
print(*ans, sep="\n")
