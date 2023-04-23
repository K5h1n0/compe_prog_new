n = int(input())
s = input()
flg = 0
for i in range(n):
    if s[i] == "o":
        flg = 1
    elif s[i] == "x":
        print("No")
        exit()
if flg == 1:
    print("Yes")
else:
    print("No")