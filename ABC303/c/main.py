n,m,h,k = map(int,input().split())
s = input()
l = []
for i in range(m):
    l.append(tuple(map(int,input().split())))
l = set(l)
nowx = 0
nowy = 0
ans = "Yes"
for i in range(len(s)):
    if s[i] == "R":
        nowx += 1
    elif s[i] == "L":
        nowx -= 1
    elif s[i] == "U":
        nowy += 1
    elif s[i] == "D":
        nowy -= 1
    h -= 1
    if h < 0:
        ans = "No"
        break
    elif (nowx,nowy) in l and h < k:
        h = k
        l.remove((nowx,nowy))
print(ans)