n = int(input())
for i in range(0,4):
    if (n + i)%5 == 0:
        print(n+i)
        exit()
    elif (n - i)% 5 == 0:
        print(n-i)
        exit()