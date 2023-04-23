n = int(input())
l1 = []
for i in range(n):
    l1.append(list(map(int,input().split())))
b = []
for i in range(n):
    b.append(list(map(int,input().split())))
l2 = list(map(list, (zip(*l1[::-1]))))
l3 = list(map(list, (zip(*l2[::-1]))))
l4 = list(map(list, (zip(*l3[::-1]))))
ans = "Yes"
for i in range(n):
    for j in range(n):
        if l1[i][j] == 1 and b[i][j] == 0:
            ans = "No"
if ans == "Yes":
    print(ans)
    exit()
ans = "Yes"
for i in range(n):
    for j in range(n):
        if l2[i][j] == 1 and b[i][j] == 0:
            ans = "No"
if ans == "Yes":
    print(ans)
    exit()
ans = "Yes"
for i in range(n):
    for j in range(n):
        if l3[i][j] == 1 and b[i][j] == 0:
            ans = "No"
if ans == "Yes":
    print(ans)
    exit()
ans = "Yes"
for i in range(n):
    for j in range(n):
        if l4[i][j] == 1 and b[i][j] == 0:
            ans = "No"
print(ans)