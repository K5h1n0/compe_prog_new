n = int(input())
l = [input() for _ in range(n)]
set1 = set(l)
l2 = list(set1)
for i in range(len(l2)):
    if l2[i][0] == "!":
        if l2[i] in set1 and l2[i][1:] in set1:
            print(l2[i][1:])
            exit()
    else:
        if l2[i] in set1 and "!"+l2[i] in set1:
            print(l2[i])
            exit()
print("satisfiable")
