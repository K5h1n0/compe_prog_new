s = input()
flg = True
for i in range(1,len(s)-1):
    flg &= s[i] == "="
if s[0] == "<" and s[-1] == ">" and flg:
    print("Yes")
else:
    print("No")