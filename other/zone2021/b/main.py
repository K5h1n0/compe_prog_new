import math

n,D,H = map(int,input().split())
l = []
for i in range(n):
    d,h = map(int,input().split())
    l.append([d,h])
maximum = math.atan2(H-0,D-0)
for i in range(len(l)):
    maximum = min(maximum,math.atan2(H-l[i][1],D-l[i][0]))
print(D-math.tan(maximum)*D)