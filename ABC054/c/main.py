import itertools

n,m = map(int,input().split())
g = [[0]*n for _ in range(n)] #隣接行列の形でグラフを保持
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    g[a][b] = 1 #辺があれば1にする
    g[b][a] = 1
ans = 0
for p in itertools.permutations(range(n)): #全部の頂点を通る順番を全列挙
    if p[0] != 0: #グラフの頂点が1から始まる時だけ調べれば良い。
        break
    flg = True
    for i in range(len(p)-1):
        flg &= g[p[i]][p[i+1]] == 1 #1ならパスがある。
    if flg:
        ans += 1
print(ans)