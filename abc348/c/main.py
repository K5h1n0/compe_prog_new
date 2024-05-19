from collections import defaultdict

n = int(input())
d = defaultdict(list)
for i in range(n):
    a,c = map(int,input().split())
    d[c].append(a)
ans = []
for v in d.values():
    v.sort()
    ans.append(v[0])
print(max(ans))