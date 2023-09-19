s = input()
if len(s) != len(set(s)):
    print("No")
    exit()
flg1 = 0
flg2 = 0
for i in range(len(s)):
    flg1 |= ord("a") <= ord(s[i]) <= ord("z")
    flg2 |= ord("A") <= ord(s[i]) <= ord("Z")
print("Yes" if flg1 and flg2 else "No")
