from time import sleep as delay

nPoint,m = map(int,input().split()) #頂点数、辺の数
sp,dp = map(int,input().split()) #スタート、ゴール
Distance = [[-1]*nPoint for _ in range(nPoint)] #隣接していない頂点と頂点の間には-1が入る。
for i in range(nPoint):
    Distance[i][i] = 0 #同一地点の場合は0が入るとのこと。
for _ in range(m):
    a,b,weight = map(int,input().split())
    Distance[a][b] = weight #隣接行列の形式で距離を保持。
    Distance[b][a] = weight
pRoute = [0] * nPoint
pDist = [10**10] * nPoint
pFixed = [False] * nPoint

#出力用の変数
sRoute = [-1] * nPoint
sDist = 10**10
print(*Distance,sep="\n")

pDist[sp] = 0
while True:
    i = 0
    while i < nPoint: #未確定の地点を一つ探す
        if not pFixed[i]:
            break
        i += 1
    if i == nPoint: #出発地から全ての地点までの最短距離が確定していれば(pFixedが全部Trueなら)、最短経路距離探索を抜ける
        break
    for j in range(i+1,nPoint): #未確定の地点の中で、スタートからの距離が最も小さい所を探す処理。
        if pFixed[j] == False and pDist[j] < pDist[i]:
            i = j
    sPoint = i
    pFixed[sPoint] = True #出発地からの最短距離を確定する
    for j in range(nPoint):
        if (Distance[sPoint][j] > 0) and not(pFixed[j]):
            newDist = pDist[sPoint] + Distance[sPoint][j]
            if newDist < pDist[j]:
                pDist[j] = newDist
                pRoute[j] = sPoint
    print(pDist,pRoute)
    delay(0.2)
sDist = pDist[dp]
j = 0
i = dp
while i != sp:
    sRoute[j] = i
    i = pRoute[i]
    j += 1
sRoute[j] = sp
print(sRoute)