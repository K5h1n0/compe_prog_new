from collections import defaultdict

n,t = map(int,input().split())
nowar = [0]*n
setnum = set()
setnum.add(0)
d = defaultdict(int)
d[0] = n
ans = []
for i in range(t):
    a,b = map(int,input().split())
    pre = nowar[a-1]
    next = pre + b
    d[pre] -= 1
    if d[pre] == 0:
        setnum.remove(pre)
    d[next] += 1
    if d[next] == 1:
        setnum.add(next)
    nowar[a-1] += b
    ans.append(len(setnum))
print(*ans,sep="\n")