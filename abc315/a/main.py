s = input()
moji = "aeiou"
ans = ""
for i in range(len(s)):
    if s[i] in moji:
        pass
    else:
        ans += s[i]
print(ans)