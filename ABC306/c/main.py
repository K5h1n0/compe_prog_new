from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
l = [[] for _ in range(n)]
for i in range(len(a)):
    l[a[i]-1].append(i)
d = defaultdict(int)
for i in range(len(l)):
    l[i].sort()
    d[l[i][1]] = i
d = sorted(list(d.items()))
ans = []
for i in range(len(d)):
    ans.append(d[i][1]+1)
print(*ans)