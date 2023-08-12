from collections import defaultdict

n = int(input())
s = list(input())
q = int(input())
l = []
d = defaultdict(tuple)
for i in range(n):
    d[i] = (-1,"a")
maxlo = -1
maxup = -1
for i in range(q):
    tmp = list(input().split())
    if tmp[0] == "2":
        maxlo = i
    elif tmp[0] == "3":
        maxup = i
    elif tmp[0] == "1":
        if d[int(tmp[1])-1][0] < i:
            d[int(tmp[1])-1] = (i,tmp[2])
if maxlo > maxup:
    flg = 0
    idx = maxlo
elif maxup > maxlo:
    flg = 1
    idx = maxup
elif maxup == -1 and maxlo == -1: # これを忘れてRE
    flg = 2
    idx = -1
for i in d:
    if d[i][0] == -1:
        if flg == 1:
            s[i] = s[i].upper()
        elif flg == 0:
            s[i] = s[i].lower()
    elif d[i] != -1:
        s[i] = d[i][1]
        if d[i][0] < idx:
            if flg == 1:
                s[i] = s[i].upper()
            elif flg == 0:
                s[i] = s[i].lower()
print("".join(s))