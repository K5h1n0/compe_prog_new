n,m,h,k = map(int,input().split())
s = input()
l = set()
for i in range(m):
    l.add(tuple(map(int,input().split())))
nowx,nowy = 0,0
for i in range(n):
    if s[i] == "R":
        nowx += 1
    elif s[i] == "L":
        nowx -= 1
    elif s[i] == "U":
        nowy += 1
    else:
        nowy -= 1
    h -= 1
    if h < 0:
        print("No")
        exit()
    elif (nowx,nowy) in l and h < k:
        l.remove((nowx,nowy))
        h = k
print("Yes")