l = []
for i in range(8):
    l.append(input())
alpha = "abcdefgh"
for i in range(8):
    for j in range(8):
        if l[i][j] == "*":
            print(alpha[j]+str(8-i))
