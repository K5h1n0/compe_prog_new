n,q = map(int,input().split())
now = []
for i in range(n,0,-1):
    now.append((i,0))
ans = []
for i in range(q):
    a,b = input().split()
    if a == "1":
        if b == "R":
            nowx = now[-1][0] + 1
            nowy = now[-1][1]
        elif b == "L":
            nowx = now[-1][0] - 1
            nowy = now[-1][1]
        elif b == "U":
            nowx = now[-1][0]
            nowy = now[-1][1] + 1
        elif b == "D":
            nowx = now[-1][0]
            nowy = now[-1][1] - 1
        now.append((nowx,nowy))
    if a == "2":
        ans.append(now[-int(b)])
for x,y in ans:
    print(x,y)