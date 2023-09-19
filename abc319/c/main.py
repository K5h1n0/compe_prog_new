import itertools

l = []
for i in range(3):
    tmp = list(map(int, input().split()))
    l += tmp
satisfy = 0
disap = 0
for v in itertools.permutations(range(0, 9), 8):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    for j in v:
        if 0 <= j <= 2:
            a.append(l[j])
        elif 3 <= j <= 5:
            b.append(l[j])
        elif 6 <= j <= 8:
            c.append(l[j])
        if j % 3 == 0:
            d.append(l[j])
        elif j % 3 == 1:
            e.append(l[j])
        elif j % 3 == 2:
            f.append(l[j])
        if j == 2 or j == 4 or j == 6:
            g.append(l[j])
        if j == 0 or j == 4 or j == 8:
            h.append(l[j])
        if (len(a) == 2 and len(set(a)) == 1) or (len(b) == 2 and len(set(b)) == 1) or (len(c) == 2 and len(set(c)) == 1) or (len(d) == 2 and len(set(d)) == 1) or (len(e) == 2 and len(set(e)) == 1) or (len(f) == 2 and len(set(f)) == 1) or (len(g) == 2 and len(set(g)) == 1) or (len(h) == 2 and len(set(h)) == 1):
            disap += 1
            break
    else:
        satisfy += 1
print(satisfy/(satisfy+disap))
