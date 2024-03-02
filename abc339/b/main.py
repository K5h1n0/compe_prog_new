h,w,n = map(int,input().split())
l = [["."]*w for _ in range(h)]
nowdir = 0
nowi = 0
nowj = 0
for i in range(n):
    if l[nowi][nowj] == ".":
        l[nowi][nowj] = "#"
        nowdir += 1
        nowdir %=4
    elif l[nowi][nowj] == "#":
        l[nowi][nowj] = "."
        nowdir -= 1
        nowdir %= 4
    if nowdir == 0:
        nowi -= 1
    elif nowdir == 1:
        nowj += 1
    elif nowdir == 2:
        nowi += 1
    elif nowdir == 3:
        nowj -= 1
    nowi %= h
    nowj %= w
for i in range(h):
    print("".join(l[i]))