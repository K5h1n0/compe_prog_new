a,b,k = map(int,input().split())
if b <= a:
    print(0)
    exit()
for i in range(1,1000000001):
    a *= k
    if b <= a:
        print(i)
        exit()