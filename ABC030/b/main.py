n,m = map(int,input().split())
if n >= 12:
    n -= 12
ans = abs((360/12*n + m/60 * 360/12)-(360/60*m))
print(min(ans,360-ans))