n = int(input())
s = list(input())
flg = 0
for i in range(n):
    if s[i] == "\"":
        flg = ~flg & 1 # いいねこの書き方
    elif flg == 0 and s[i] == ",":
        s[i] = "."
print(*s,sep="")