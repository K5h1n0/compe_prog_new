#考え方の解法を見てしまった……。

h,w = map(int,input().split())
l_x = []
l_x.append([0] * (w+1))
for i in range(h):
    l_tmp = [0] + list(map(int,input().split()))
    tmp = 0
    for j in range(w+1):
        tmp += l_tmp[j]
        l_tmp[j] = tmp
    l_x.append(l_tmp)
for j in range(w+1):
    tmp = 0
    for i in range(h+1):
        tmp += l_x[i][j]
        l_x[i][j] = tmp
q = int(input())
ans = []
for i in range(q):
    a,b,c,d = map(int,input().split())
    #二次元累積和は、足し引きがミソ。大きい四角-縦の四角-横の四角+小さい四角。
    ans_int = l_x[c][d] - l_x[c][b-1] - l_x[a-1][d] + l_x[a-1][b-1]
    ans.append(ans_int)
print(*ans,sep="\n")