s = input()
i = 0
flg = False
ans = 0
while i < len(s):
    if s[i] == "0" and not flg:
        flg = True
    elif s[i] == "0" and flg:
        flg = False
        ans += 1
    else:
        if flg:
            ans += 1
        flg = False
        ans += 1
    i += 1
if s[-1] == "0" and flg:
    ans += 1
print(ans)
