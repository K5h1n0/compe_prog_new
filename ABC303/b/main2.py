n,m = map(int,input().split())
a = []
for i in range(m):
    a.append(list(map(int,input().split())))
l = [[1]*n for _ in range(n)] #最後にsumで答えを求める為に、1で初期化。
for i in range(n):
    l[i][i] = 0
for i in range(m):
    for j in range(n-1):
        l[a[i][j]-1][a[i][j+1]-1] = 0 #隣り合う人同士なら0にする。
        l[a[i][j+1]-1][a[i][j]-1] = 0
print(sum(map(sum,l))//2) #二次元配列の合計を求める時