import math

x1,y1,x2,y2,t,v = map(int,input().split())
n = int(input())
ans = "NO"
for i in range(n):
    tmpx,tmpy = map(int,input().split())
    d1 = math.sqrt((tmpx-x1)**2 + (tmpy-y1)**2)
    d2 = math.sqrt((x2-tmpx)**2 + (y2-tmpy)**2)
    if t * v >= d1 + d2:
        ans = "YES"
print(ans)