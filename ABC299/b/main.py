n,t = map(int,input().split())
c = list(map(int,input().split()))
r = list(map(int,input().split()))
c_set = set(c)
if t in c_set:
    color = t
    minimum = -1
else:
    color = c[0]
    minimum = r[0]
ans = 1
for i in range(n):
    if c[i] == color and minimum < r[i]:
        minimum = r[i]
        ans = i+1
print(ans)