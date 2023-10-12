from collections import defaultdict

n = int(input())
l = []
for i in range(1,n+1):
    tmp = list(input())
    cnt = 0
    for j in range(n):
        if tmp[j] == "o":
            cnt += 1
    l.append((cnt,i))
d = defaultdict(list)
for i,v in l:
    d[i].append(v)
for i in d:
    d[i].sort()
ans = []
for i in range(n,-1,-1):
    if len(d[i]) == 0:
        continue
    for j in d[i]:
        ans.append(j)
print(*ans)