from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
total = 0
for i in range(2,n,2):
    total += a[i] - a[i-1]
q = int(input())
log = []
numlist = set(a[:])
for i in range(q):
    l,r = map(int,input().split())
    log.append([l,r])
    numlist.add(l)
    numlist.add(r)
numlist = sorted(list(numlist))
d = defaultdict(int)
for i, v in enumerate(numlist):
    d[v] = i
lflg = [0]*len(numlist)
for i in range(len(a)):
    if i%2:
        lflg[d[a[i]]] = 1
    else:
        lflg[d[a[i]]] = 9
accum = []
flg = 1
memory = numlist[-1]
for i in range(len(lflg)-1,-1,-1):
    if flg == 0:
        if lflg[i] == 9:
            memory = numlist[i]
            accum.append(0)
            flg = 1
        elif lflg[i] == 0:
            accum.append(0)
    elif flg == 1:
        if lflg[i] == 0:
            accum.append(memory-numlist[i])
            memory = numlist[i]
        elif lflg[i] == 1:
            accum.append(memory-numlist[i])
            memory = 0
            flg = 0
accum.append(0)
accum.reverse()
for i in range(1,len(accum)):
    accum[i] += accum[i-1]
ans = []
for i in range(len(log)):
    time = accum[d[log[i][1]]] - accum[d[log[i][0]]]
    ans.append(time)
print(*ans,sep="\n")