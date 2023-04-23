h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
ans = 0
for i in range(h):
    for j in range(w-1):
        if l[i][j] == "." and l[i][j+1] == ".":
            ans += 1
for i in range(w):
    for j in range(h-1):
        if l[j][i] == "." and l[j+1][i] == ".":
            ans += 1
print(ans)