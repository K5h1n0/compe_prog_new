n,m = map(int,input().split())
l = []
for i in range(n):
    p,c,*f = map(int,input().split())
    l.append([p,c,f])
flg = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        iset = set(l[i][2])
        jset = set(l[j][2])
        flg |= l[i][0] >= l[j][0] and jset >= iset and (l[i][0] > l[j][0] or len(jset) > len(iset))
if flg:
    print("Yes")
else:
    print("No")