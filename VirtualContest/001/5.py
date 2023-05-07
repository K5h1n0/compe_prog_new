h,w = map(int,input().split())
l = []
for i in range(h):
    tmp = input()
    l.append(tmp)
    l.append(tmp)
for i in range(len(l)):
    print(*l[i],sep="")