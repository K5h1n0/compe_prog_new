import math

n = int(input())
l = []
for i in range(n):
    tmp = list(map(int,input().split()))
    l.append(tmp)
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            l = [(((l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2)**0.5), (((l[i][0]-l[k][0])**2 + (l[i][1]-l[k][1])**2)**0.5), (((l[j][0]-l[k][0])**2 + (l[j][1]-l[k][1])**2)**0.5)]
            l.sort()
            if not math.isclose(l[2], l[0] + l[1]):
                ans += 1
print(ans)