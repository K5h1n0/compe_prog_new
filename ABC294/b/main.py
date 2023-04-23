h,w = map(int,input().split())
l = []
for i in range(h):
    tmp = list(map(int,input().split()))
    tmps = ""
    for j in range(len(tmp)):
        if tmp[j] == 0:
            tmps += "."
        else:
            tmps += chr(ord("A")-1 + tmp[j])
    l.append(tmps)
for i in range(len(l)):
    print(l[i])