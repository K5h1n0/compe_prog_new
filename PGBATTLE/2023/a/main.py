a,b,c,d,l,r = map(int,input().split())
if 0 <= abs(a*l**3 + b*l**2 + c*l + d) < 0.0000000001:
    print(float(l))
    exit()
if 0 <= abs(a*r**3 + b*r**2 + c*r + d) < 0.0000000001:
    print(float(r))
    exit()

while r - l > 0.0000000001:
    print("r,l,r-l",r,l,r-l)
    mid = (l + r) / 2
    print("mid",mid)
    if a*mid**3 + b*mid**2 + c*mid + d < 0:
        l = mid
    else:
        r = mid
print(l)