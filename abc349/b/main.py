from collections import defaultdict
s = input()
d = defaultdict(int)
for i in range(len(s)):
    d[s[i]] += 1
count = defaultdict(int)
for i in d.values():
    count[i] += 1
flg = True
for i in count.values():
    flg &= i == 2
print("Yes" if flg else "No")