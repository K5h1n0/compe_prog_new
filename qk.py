# https://www.youtube.com/watch?v=4mh9qsH0Zhs

import itertools

n = int(input())
a = list(map(int, input().split()))
x = float(input())
ans = []
for v in itertools.permutations(range(n), n):
    tmp = []
    tmp.append((a[v[0]]+a[v[1]], str(a[v[0]])+"+"+str(a[v[1]])))
    tmp.append((a[v[0]]-a[v[1]], str(a[v[0]])+"-"+str(a[v[1]])))
    tmp.append((a[v[0]]*a[v[1]], str(a[v[0]])+"*"+str(a[v[1]])))
    tmp.append((a[v[0]]/a[v[1]], str(a[v[0]])+"/"+str(a[v[1]])))
    for i in range(2, n):
        tmp2 = tmp[:]
        tmp = []
        for tuple in tmp2:
            tmp.append((tuple[0]+a[v[i]], tuple[1]+"+"+str(a[v[i]])))
            tmp.append((tuple[0]-a[v[i]], tuple[1]+"-"+str(a[v[i]])))
            tmp.append((tuple[0]*a[v[i]], "("+tuple[1]+")*"+str(a[v[i]])))
            tmp.append((tuple[0]/a[v[i]], "("+tuple[1]+")/"+str(a[v[i]])))
    for tuple in tmp:
        if x == tuple[0]:
            print(tuple[1])
            exit()
print("Nothing")
