s = input()
if s == "AtCoder":
    print("Yes")
    exit()
capi = "ATCODER"
lower = "atcoder"
flg = True
for i in range(7):
    flg &= s[i] == capi[i] or s[i] == lower[i]
if flg:
    print("Maybe")
else:
    print("No")