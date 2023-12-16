import itertools

n,m = map(int,input().split())
d = [[-1]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
maximum = 0
for p in itertools.permutations(range(n)):
    now = 0
    for i in range(len(p)-1):
        if d[p[i]][p[i+1]] == -1:
            maximum = max(maximum,now)
            break
        now += d[p[i]][p[i+1]]
    else:
        maximum = max(maximum,now)
print(maximum)