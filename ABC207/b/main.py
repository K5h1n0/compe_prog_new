#解説ACよく分からない

a,b,c,d = map(int,input().split())
blue = a
red = 0
for i in range(1,a+1):
    blue += b
    red += c
    if blue <= d*red:
        print(i)
        exit()
print(-1)