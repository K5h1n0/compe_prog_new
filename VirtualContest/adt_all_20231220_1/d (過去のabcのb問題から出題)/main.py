h,m = map(int,input().split())
for i in range(86400):
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    if 0 <= int(h[0]+m[0]) <= 23 and 0 <= int(h[1]+m[1]) <= 59:
        print(h,m)
        exit()
    m = int(m) + 1
    h = int(h)
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0