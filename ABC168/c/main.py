import math
a,b,h,m = map(int,input().split())
angle_m = m/60*360
angle_h = (h/12 + angle_m/360/12) *360
angle = min(max(angle_h,angle_m)-min(angle_h,angle_m),360-(max(angle_h,angle_m)-min(angle_h,angle_m)))
#余弦定理
ans = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle)))
#pythonのsinやcosはパイラジアンに変換してから
print(ans)