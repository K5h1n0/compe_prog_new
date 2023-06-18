n,w = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort(reverse=True)
ans = 0
for i in range(len(l)):
    if 0 <= w - l[i][1]:
        ans += l[i][0]*l[i][1]
        w -= l[i][1]
    else:
        ans += l[i][0]*w
        break
print(ans)