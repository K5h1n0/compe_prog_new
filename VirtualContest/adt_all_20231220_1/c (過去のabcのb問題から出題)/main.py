n = int(input())
l = []
for i in range(n):
    l.append(list(input()))
flg = True
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if l[i][j] == "D" and l[j][i] == "D":
            flg &= True
        elif l[i][j] == "W" and l[j][i] == "L":
            flg &= True
        elif l[i][j] == "L" and l[j][i] == "W":
            flg &= True
        else:
            flg &= False
if flg:
    print("correct")
else:
    print("incorrect")