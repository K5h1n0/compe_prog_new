n,h,w = map(int,input().split())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b,a*b])
total = h*w
for i in range(2**n):
    now = []
    cnt = 0
    for j in range(n):
        if ((i>>j) & 1):
            now.append(l[j])
            cnt += l[j][2]
    if total != cnt:
        continue
    print(now)
    length = len(now)
    