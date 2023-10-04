n = int(input())
if 1 <= n%40 <= 20:
    if n%20 == 0:
        print(20)
    else:
        print(n%20)
else:
    print((20-n)%20+1)