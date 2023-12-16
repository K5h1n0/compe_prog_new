import itertools

n,k = map(int,input().split())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
ans = 0
for p in itertools.permutations(range(n)):
    if p[0] != 0:
        break
    now = 0
    for i in range(n-1):
        now += l[p[i]][p[i+1]]
    now += l[p[-1]][p[0]]
    ans += now == k
print(ans)