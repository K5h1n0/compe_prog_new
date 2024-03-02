s = input()
flg = True
flg &= ord("A") <= ord(s[0]) <= ord("Z")
for i in range(1,len(s)):
    flg &= ord("a") <= ord(s[i]) <= ord("z")
print("Yes" if flg else "No")