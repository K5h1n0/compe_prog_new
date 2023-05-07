n = input()
ans = 0
for i in range(2**len(n)):
    l1 = []
    l2 = []
    for j in range(len(n)):
        if ((i>>j) & 1):
            l1.append(n[j])
        else:
            l2.append(n[j])
    if l1 == [] or l2 == []:
        continue
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    tmp = int("".join(l1))*int("".join(l2))
    if ans < tmp:
        ans = tmp
print(ans)
