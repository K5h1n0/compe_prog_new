n,d = map(int,input().split())
l = []
ans = 0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        total = 0
        for k in range(d):
            total += (l[i][k] - l[j][k])**2
        if total**0.5%1 == 0:
            ans += 1
print(ans)