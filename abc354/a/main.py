h = int(input())
now = 0
for i in range(100):
    now += 2**i
    if h < now:
        print(i+1)
        exit()