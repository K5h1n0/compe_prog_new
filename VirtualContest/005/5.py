import math

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
ans = 0
for i in range(len(l)):
    s = (l[i]**2)*math.pi
    if i % 2 == 0:
        ans += s
    else:
        ans -= s
print(ans)