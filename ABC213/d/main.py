#解説見ながら
#オイラーツアーと呼ぶらしい。

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n = int(input())
d = defaultdict(list)
ans = []
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

# 問題文から、都市番号の小さい順に回るため、ここのソートは必要。
for i in range(len(d)+1): #range(0,len(d))にすると、defaultdictに勝手に0というキーが追加されてしまうので、1スタート。
    d[i].sort()

def dfs(now,pre):
    ans.append(now)

    for to in d[now]: #やっぱりdfsでもfor文は必要なんだなという気持ち
        if to != pre:
            dfs(to,now)
            ans.append(now) #関数の中で再度関数を呼び出した後に実行する命令を書くこともあるのか。

dfs(1,-1) #最初の起爆剤として、今いる都市1を入れる。都市1の前は無いので、存在しない都市-1を仮に入れておくらしい。
print(*ans)