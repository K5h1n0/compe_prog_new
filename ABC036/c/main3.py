n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a2 = sorted(set(a[:]))
d = {}
for i, v in enumerate(a2):
    d[v] = i
for i in range(n):
    print(d[a[i]])
