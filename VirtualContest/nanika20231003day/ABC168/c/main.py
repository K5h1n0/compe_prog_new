import math

a, b, h, m = map(int, input().split())
hangle = (h % 12)*30+0.5*m
mangle = m/60*360
ans = (a**2 + b**2 - 2 * a*b * math.cos(math.radians(abs(hangle-mangle))))**0.5
print(ans)
