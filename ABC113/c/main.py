from collections import defaultdict

n, m = map(int, input().split())
l = []
d = defaultdict(list)
for i in range(m):
    p, y = map(int, input().split())
    d[p].append(y)
    l.append([p, y])
d2 = defaultdict(dict)
for i in d:
    tmp = sorted(set(d[i]))
    for j, v in enumerate(tmp):
        d2[i][v] = j+1
for i in range(m):
    print(str(l[i][0]).zfill(6)+str(d2[l[i][0]][l[i][1]]).zfill(6))
