n = int(input())
l = []
l10 = []
for i in range(n):
    tmp = int(input())
    if tmp%10 == 0:
        l10.append(tmp)
    else:
        l.append(tmp)
if (sum(l) + sum(l10))%10 != 0:
    print(sum(l)+sum(l10))
    exit()
if len(l) == 0:
    print(0)
    exit()
l.sort()
l = l[1:]
print(sum(l)+sum(l10))