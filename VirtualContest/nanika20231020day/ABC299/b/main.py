n,t = map(int,input().split())
c = list(map(int,input().split()))
r = list(map(int,input().split()))
cset = set(c[:])
if t in cset:
    ans = 0
    maximum = 0
    for i in range(n):
        if c[i] == t and maximum < r[i]:
            ans = i + 1
            maximum = r[i]
    print(ans)
else:
    ans = 1
    t = c[0]
    maximum = r[0]
    for i in range(1,n):
        if c[i] == t and maximum < r[i]:
            ans = i + 1
            maximum = r[i]
    print(ans)