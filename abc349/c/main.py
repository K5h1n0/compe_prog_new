s = input().upper()
t = input()
if t[-1] == "X":
    flg = 0
    for i in range(len(s)):
        if flg == 0 and t[flg] == s[i]:
            flg = 1
        elif flg == 1 and t[flg] == s[i]:
            flg = 2
            break
    if flg == 2:
        print("Yes")
    else:
        print("No")
else:
    flg = 0
    for i in range(len(s)):
        if flg == 0 and t[flg] == s[i]:
            flg = 1
        elif flg == 1 and t[flg] == s[i]:
            flg = 2
        elif flg == 2 and t[flg] == s[i]:
            flg = 3
            break
    if flg == 3:
        print("Yes")
    else:
        print("No")