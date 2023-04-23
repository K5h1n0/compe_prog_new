from collections import defaultdict

n = int(input())
q = int(input())
b = []
for i in range(n+1):
    b.append([])
d = defaultdict(set)
ans = []
for i in range(q):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        b[tmp[2]].append(tmp[1])
        d[tmp[1]].add(tmp[2])
    elif tmp[0] == 2:
        ans.append(sorted(b[tmp[1]]))
    else:
        ans.append(sorted(list(d[tmp[1]])))
for i in ans:
    print(*i)