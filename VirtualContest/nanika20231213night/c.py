from collections import defaultdict
import itertools

n,m = map(int,input().split())
ab = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    ab[a][b] = 1
    ab[b][a] = 1
cd = [[0]*n for _ in range(n)]
for _ in range(m):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    cd[c][d] = 1
    cd[d][c] = 1
for p in itertools.permutations(range(n)):
    flg = True
    for i in range(n):
        for j in range(n):
            flg &= cd[i][j] == ab[p[i]][p[j]]
    if flg:
        print("Yes")
        exit()
print("No")