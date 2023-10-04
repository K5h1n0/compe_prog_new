h, w, n = map(int, input().split())
li = []
lj = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    li.append(a)
    lj.append(b)

seti = sorted(set(li))
setj = sorted(set(lj))

D = {v: i for i, v in enumerate(seti)}
print(D)
