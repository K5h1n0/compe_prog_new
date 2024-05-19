x = int(input())
now = 0
for i in range(1,100001):
    now += i
    if x <= now:
        print(i)
        exit()