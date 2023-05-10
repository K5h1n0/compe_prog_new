import copy

n = int(input())
s = list(input())
s2 = copy.copy(s)
s2.reverse()
if s == s2:
    print("Yes")
    exit()
if len(s) == 2:
    if s[0] == s[1]:
        print("Yes")
    else:
        print("No")
    exit()
if s[0] == "B":
    print("Yes")
elif s[-1] == "A":
    print("Yes")
else:
    print("No")