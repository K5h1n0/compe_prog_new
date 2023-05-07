#解説AC
#しゃくとり法かと思いきや、辞書型を使って差分計算を行なっていく。
from collections import defaultdict

n,k = map(int,input().split())
c = list(map(int,input().split()))

d = defaultdict(int)
kinds = 0
for i in range(k):
    if d[c[i]] == 0: # 0から1へ変わるときのみ、kinds+=1
        kinds += 1
    d[c[i]] += 1
ans = kinds

for i in range(n-k):
    if d[c[i+k]] == 0:
        kinds += 1
    d[c[i+k]] += 1
    
    if d[c[i]] == 1:
        kinds -= 1
    d[c[i]] -= 1
    ans = max(ans,kinds)
print(ans)