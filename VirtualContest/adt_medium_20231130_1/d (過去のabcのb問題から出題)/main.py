n = int(input())
now = 2
for i in range(61):
    if n < 2 ** i:
        print(i-1)
        exit()