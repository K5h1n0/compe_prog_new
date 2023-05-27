s = input()
ans = ""
for i in range(len(s)-1,-1,-1):
    if s[i] == "0":
        ans += "0"
    elif s[i] == "1":
        ans += "1"
    elif s[i] == "6":
        ans += "9"
    elif s[i] == "8":
        ans += "8"
    elif s[i] == "9":
        ans += "6"
print(ans)