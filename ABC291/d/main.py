n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
kakunou = []
if l[0][0] == l[0][1]:
    kakunou.append(1)
else:
    kakunou.append(2)
tmpa = l[0][0]
tmpb = l[0][1]
for i in range(1,n):
    l2 = set([tmpa,tmpb,l[i][0],l[i][1]])
    length = len(l2)
    if length == 4:
        kakunou.append(2)
    elif length == 3:
        if l[i][0] == l[i][1]:
            kakunou.append(1)
        else:
            kakunou.append(2)
    elif length == 2:
        if l[i][0] != l[i][1]:
            kakunou.append(2)
        else:
            kakunou.append(1)
    elif length == 1:
        kakunou.append(0)
    tmpa = l[i][0]
    tmpb = l[i][1]
print(kakunou)
now = 1
for i in range(len(kakunou)):
    now *= kakunou[i]
    now %= 998244353
print(now)