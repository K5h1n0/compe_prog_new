n = int(input())
s = input()
flg = 0
ans = "out"
for i in range(n):
    if flg == 0 and s[i] == "|":
        flg += 1
    elif flg == 1 and s[i] == "*":
        flg += 1
    elif flg == 2 and s[i] == "|":
        ans = "in"
print(ans)