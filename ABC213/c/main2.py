h, w, n = map(int, input().split())
li1 = []
lj1 = []
for i in range(n):
    a, b = map(int, input().split())
    li1.append(a)
    lj1.append(b)
li2 = sorted(set(li1[:]))
lj2 = sorted(set(lj1[:]))
di = {}
dj = {}
for i, v in enumerate(li2):
    di[v] = i+1
for i, v in enumerate(lj2):
    dj[v] = i+1
for i in range(n):
    print(di[li1[i]], dj[lj1[i]])
