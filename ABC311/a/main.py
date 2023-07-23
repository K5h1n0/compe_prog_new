n = int(input())
s = input()
l = [0,0,0]
for i in range(n):
    if s[i] == "A":
        l[0] = 1
    elif s[i] == "B":
        l[1] = 1
    elif s[i] == "C":
        l[2] = 1
    if sum(l) == 3:
        print(i+1)
        exit()