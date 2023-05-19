import copy

l1 = []
for i in range(3):
    tmp = list(map(int,input().split()))
    l1.append(tmp)
l2 = copy.deepcopy(l1)
ans = "No"
for i in range(0,101):
    for j in range(0,101):
        for k in range(0,101):
            for m in range(3):
                l2[m][0] = l1[m][0] - i
                l2[m][1] = l1[m][1] - j
                l2[m][2] = l1[m][2] - k
            if l2[0][0] == l2[0][1] == l2[0][2] and l2[1][0] == l2[1][1] == l2[1][2] and l2[2][0] == l2[2][1] == l2[2][2]:
                ans = "Yes"
                break
print(ans)