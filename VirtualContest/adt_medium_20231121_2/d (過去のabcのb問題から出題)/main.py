s = input()
t = input()
flg = False
for i in range(26):
    now = []
    for j in range(len(t)):
        now.append(chr((ord(s[j]) + i)%26+97))
    now = "".join(now)
    flg |= now == t
print("Yes" if flg else "No")