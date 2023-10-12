s = input()
flg = True
for i in range(len(s)):
    if i%2 == 1:
        flg &= s[i] == "0"
if flg:
    print("Yes")
else:
    print("No")