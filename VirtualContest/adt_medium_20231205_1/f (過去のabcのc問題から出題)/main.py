n = int(input())
a = sorted(list(map(int,input().split())))
length = len(a)
now = 1
i = 0
while 1 < length and i < length:
    if now == a[i]:
        now += 1
        i += 1
    else:
        a.pop()
        a.pop()
        now += 1
    length = len(a)
    print(i,now,a)
print(now)