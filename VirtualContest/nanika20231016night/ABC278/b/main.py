h,m = input().split()
for i in range(1441):
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    if 0 <= int(h[0]+m[0]) <= 23 and 0 <= int(h[1]+m[1]) <= 59:
        print(h,m)
        exit()
    m = int(m)+1
    h = int(h)
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0