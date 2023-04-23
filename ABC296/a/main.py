n = int(input())
s = list(input())
if n == 1:
    print("Yes")
else:
    l1 = []
    l2 = []
    for i in range(n):
        if i % 2 == 0:
            l1.append(s[i])
        else:
            l2.append(s[i])
    if len(set(l1)) == 1 and len(set(l2)) == 1:
        print("Yes")
    else:
        print("No")