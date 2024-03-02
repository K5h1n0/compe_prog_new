n = int(input())
q = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
qmax = max(q)
l = []
for anum in range(qmax+1):
    flg = True
    bnummin = 10**10
    for j in range(n):
        left = q[j] - a[j]*anum
        if left < 0:
            flg = False
            break
        if b[j] == 0:
            continue
        bnum = left // b[j]
        bnummin = min(bnummin,bnum)
    if flg:
        l.append(bnummin+anum)
print(max(l))