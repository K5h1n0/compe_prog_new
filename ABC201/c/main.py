#自力で解けたけど解説見ながら綺麗なコードを書いたほうが良い。
from collections import defaultdict

s = input()
use = set()
not_use = set()
d = defaultdict(int)
for i in range(10):
    if s[i] == "o":
        use.add(str(i))
        d[str(i)] = 0
    elif s[i] == "x":
        not_use.add(str(i))
if len(use) == 0:
    flg = 1
else:
    flg = 0
cnt = 0
if 4 < len(use):
    print(cnt)
    exit()
number = ["0","1","2","3","4","5","6","7","8","9"]
for i in number:
    for j in number:
        for k in number:
            for m in number:
                if i in not_use or j in not_use or k in not_use or m in not_use:
                    continue
                if flg == 0:
                    for o in use:
                        d[o] = 0
                    if i in d:
                        d[i] += 1
                    if j in d:
                        d[j] += 1
                    if k in d:
                        d[k] += 1
                    if m in d:
                        d[m] += 1
                    if 0 == min(d.values()):
                        continue
                cnt += 1
print(cnt)