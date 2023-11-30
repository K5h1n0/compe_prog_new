n = int(input())
a = sorted(list(map(int,input().split())))
if n%2:
    print(a[n//2])
else:
    print((a[n//2-1]+a[n//2])*10//2/10)