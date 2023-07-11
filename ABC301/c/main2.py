#解説AC
#https://programming-hiroba.com/abc301-c/

from collections import defaultdict

s = input()
t = input()

ds = defaultdict(int)
dt = defaultdict(int)
for i in range(len(s)):
    ds[s[i]] += 1
    dt[t[i]] += 1
print(ds)
print(dt)
result = True
for ch in "abcdefghijklemopqrstuvwxyz":
    if ch in "atcoder":
        if ds[ch] > dt[ch]:
            dt["@"] -= ds[ch] - dt[ch]
        elif ds[ch] < dt[ch]:
            ds["@"] -= dt[ch] - ds[ch]
    else: #chが"atcoder"という文字のいずれでも無い場合は、sとtでそのアルファベットの個数が異なっていたら、その瞬間にいくら@のカードを使用しても揃えることができない。
        if ds[ch] != dt[ch]:
            result = False
            break
if ds["@"] < 0 or dt["@"] < 0:
    result = False

print("Yes" if result else "No")