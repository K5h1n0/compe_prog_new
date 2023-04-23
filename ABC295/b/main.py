from functools import lru_cache
r,c = map(int,input().split())

@lru_cache(maxsize=1000)
def f(m):
    m += 1
    list_ij = []
    for i in range(m):
        for j in range(m):
            if i + j < m:
                list_ij.append((i,j))
                list_ij.append((-i,j))
                list_ij.append((i,-j))
                list_ij.append((-i,-j))
    list_ij = list(set(list_ij))
    return list_ij

l = []
l2 = []
for i in range(r):
    tmp = list(input())
    a = []
    for j in range(len(tmp)):
        if tmp[j] != "." and tmp[j] != "#":
            a.append(".")
            l2.append([int(tmp[j]),i,j])
        else:
            a.append(tmp[j])
    l.append(a)
ans = []
for i in range(len(l2)):
    bomb = l2[i][0]
    y = l2[i][1]
    x = l2[i][2]
    for j in f(bomb):
        if 0 <= y + j[0] and y + j[0] < r and 0 <= x + j[1] and x + j[1] < c:
            l[y+j[0]][x+j[1]] = "."
for i in range(len(l)):
    print(*l[i],sep="")