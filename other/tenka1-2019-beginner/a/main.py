a,b,c = map(int,input().split())
if a > b:
    a *= -1
    b *= -1
    c *= -1
if a < c < b:
    print("Yes")
else:
    print("No")