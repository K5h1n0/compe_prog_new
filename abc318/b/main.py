n = int(input())
l = [[0]*110 for _ in range(110)]
for i in range(n):
    a, b, c, d = map(int, input().split())
    l[a][c] += 1
    l[b][c] -= 1
    l[a][d] -= 1
    l[b][d] += 1
for i in range(110):
    for j in range(1, 110):
        l[i][j] += l[i][j-1]
for j in range(110):
    for i in range(1, 110):
        l[i][j] += l[i-1][j]
ans = 0
for i in range(110):
    for j in range(110):
        if l[i][j] != 0:
            ans += 1
print(ans)
