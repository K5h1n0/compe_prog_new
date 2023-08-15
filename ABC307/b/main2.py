n = int(input())
l = []
for i in range(n):
    l.append(input())
flg = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        str1 = l[i]+l[j]
        str2 = str1[::-1]
        flg |= str1 == str2
print("Yes" if flg else "No")