# 解説AC
"""
https://atcoder.jp/contests/abc224/editorial/2810
https://mathwords.net/x1y2hikux2y1
"""

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if abs((l[j][0] - l[i][0])*(l[k][1] - l[i][1]) - (l[k][0] - l[i][0])*(l[j][1] - l[i][1])) * 0.5 != 0:
                ans += 1
print(ans)