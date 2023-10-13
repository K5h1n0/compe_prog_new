a = input()
b = input()
c = input()
s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "1":
        ans += a
    elif s[i] == "2":
        ans += b
    else:
        ans += c
print(ans)