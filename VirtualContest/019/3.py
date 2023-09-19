s = input()
ans = 0
flg = 0
for i in range(len(s)):
    if s[i] == "0" and flg == 0:
        flg = 1
        continue
    elif s[i] == "0" and flg == 1:
        ans += 1
        flg = 0
    else:
        ans += 1
        if flg == 1:
            ans += 1
            flg = 0
if flg == 1:
    ans += 1
print(ans)