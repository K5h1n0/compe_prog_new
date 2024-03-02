from collections import defaultdict

s = input()
d = defaultdict(int)
for i in s:
    d[i] += 1
tmp = []
for i in d.items():
    tmp.append((i[1],i[0]))
tmp.sort()
for i in range(len(s)):
    if s[i] == tmp[0][1]:
        print(i+1)
        exit()