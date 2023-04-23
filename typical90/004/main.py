h,w = map(int,input().split())
l1 = []
l2 = []
for i in range(h):
    row = list(map(int,input().split()))
    l1.append(row)
    l2.append(sum(row))
l3 = []
for i in range(w):
    total = 0
    for j in range(h):
        total += l1[j][i]
    l3.append(total)
l4 = []
for i in range(h):
    l4.append([])
    for j in range(w):
        l4[i].append(l2[i]+l3[j]-l1[i][j])
for i in range(h):
    print(*l4[i])