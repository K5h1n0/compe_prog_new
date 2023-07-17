n = int(input())
l = []
for i in range(n):
    tmp1 = input()
    tmp2 = tmp1[::-1]
    tmp3 = sorted([tmp1,tmp2])
    l.append(tmp3[0])
print(len(set(l)))