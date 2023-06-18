n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l2 = l[:]
l2.sort(reverse=True)
tmp1 = l2[0]
tmp2 = l2[1]
for i in range(n):
    if tmp1 != tmp2 and l[i] == tmp1:
        print(tmp2)
    elif tmp1 != tmp2 and l[i] == tmp2:
        print(tmp1)
    else:
        print(tmp1)