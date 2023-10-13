from collections import defaultdict

x= input()
d = defaultdict(int)
d2 = defaultdict(str)
for i,v in enumerate(list(x)):
    d[v] = i
    d2[i] = v
n = int(input())
s = []
for i in range(n):
    inp = input()
    new = []
    for i in inp:
        new.append(d[i])
    s.append(new)
s.sort()
ans = []
for i in range(len(s)):
    now = ""
    for j in range(len(s[i])):
        now += d2[s[i][j]]
    ans.append(now)
print(*ans,sep="\n")