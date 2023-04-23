s = input()
ans = "Yes"
flg = 0
flg2 = 0
for i in range(len(s)):
    if s[i] == "B" and i % 2 == 0:
        flg += 1
    elif s[i] == "B" and i % 2 == 1:
        flg += 2
if flg != 3:
    ans = "No"
else:
    for i in range(len(s)):
        if flg2 == 0 and s[i] == "R":
            flg2 += 1
        elif flg2 == 1 and s[i] == "K":
            flg2 += 1
        elif flg2 == 2 and s[i] == "R":
            flg2 += 1
if flg2 != 3:
    ans = "No"
print(ans)