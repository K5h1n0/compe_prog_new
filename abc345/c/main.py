from collections import defaultdict
s = input()
d = defaultdict(int)
total = len(s) * (len(s)-1) // 2
for i in range(len(s)):
    d[s[i]] += 1
minus = 0
flg = 0
for i in d.values():
    if flg == 0 and 2 <= i:
        flg = 1
    minus += (i * (i - 1) //2)
print(total-minus+flg)