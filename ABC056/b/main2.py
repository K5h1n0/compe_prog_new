w,a,b = map(int,input().split())
if b < a:
    a,b = b,a
if a + w < b:
    print(b-a-w)
else:
    print(0)