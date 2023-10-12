n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        x = l[i][0] - l[j][0]
        if x == 0:
            continue
        y = l[i][1] - l[j][1]
        slope = y/x
        if -1 <= slope <= 1:
            ans += 1
print(ans)