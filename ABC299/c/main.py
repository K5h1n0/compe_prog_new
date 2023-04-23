n = int(input())
s = input()
flg = 0
ans = -1
cnt = 0
for i in range(n):
    if flg == 0:
        if s[i] == "o":
            cnt = 1
            flg = 1
        else:
            pass
    elif flg == 1:
        if s[i] == "o":
            cnt += 1
        else:
            ans = max(ans,cnt)
            cnt = 0
            flg = 0
flg = 0
cnt = 0
for i in range(n-1,-1,-1):
    if flg == 0:
        if s[i] == "o":
            cnt = 1
            flg = 1
        else:
            pass
    elif flg == 1:
        if s[i] == "o":
            cnt += 1
        else:
            ans = max(ans,cnt)
            cnt = 0
            flg = 0
print(ans)