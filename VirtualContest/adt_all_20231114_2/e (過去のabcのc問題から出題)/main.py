from collections import defaultdict

x = input()
d1 = defaultdict(int)
d2 = defaultdict(int)
for i in range(26):
    d1[x[i]] = i
    d2[i] = x[i]
n = int(input())
s = []
for i in range(n):
    inp = list(input())
    now = []
    for j in range(len(inp)):
        now.append(d1[inp[j]])
    s.append(now)
s.sort()
ans = []
for i in range(len(s)):
    nowans = ""
    for j in s[i]:
        nowans += d2[j]
    ans.append(nowans)
print(*ans,sep="\n")