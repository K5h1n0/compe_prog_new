import math

a, b, h, m = map(int, input().split())
h_angle = (h % 12)*30 + 0.5*m
m_angle = m*6
ans = (a**2+b**2 - 2 * a * b *
       math.cos(math.radians(abs(h_angle-m_angle))))**0.5
print(ans)
