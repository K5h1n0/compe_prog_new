h,w = map(int,input().split())
x = []
for i in range(h):
    x.append(list(map(int,input().split())))
ans = [[],[],[]]
for i in range(h):
    for j in range(w):
        if x[i][j] != 0:
            ans[0].append(i+1)
            ans[1].append(j+1)
            ans[2].append(x[i][j])
for i in range(3):
    print(*ans[i])
"""

# テストケース出力
import random
n = 3
m = 4
print(n,m)
l = []
for i in range(n):
    tmp = []
    for j in range(m):
        if random.randrange(0,2) == 0:
            tmp.append(random.randrange(1,5))
        else:
            tmp.append(0)
    l.append(tmp)
for i in l:
    print(*i)
"""