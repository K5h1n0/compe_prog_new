s = input()
k = int(input())

if k < len(s):
    ans = 0
    flg = 1
    for i in range(k):
        if s[i] == "1":
            continue
        else:
            flg = 0
            ans = s[i]
            break
    if flg == 1:
        print(1)
    else:
        print(ans)
    exit()
ans = 0
for i in range(len(s)):
    if s[i] == "1":
        continue
    else:
        ans = s[i]
        break
if ans == 0:
    print(1)
else:
    print(ans)