n,m = map(int,input().split())
s = []
for i in range(n):
    s.append(input())
t = []
for i in range(m):
    t.append(input())
ans = 0
for i in range(n):
    flg = False
    for j in range(m):
        flg |= s[i][3:] == t[j]
    if flg:
        ans += 1
print(ans)