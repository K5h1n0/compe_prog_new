n = int(input())
s = list(input())
k = int(input())
character = s[k-1]
ans = ""
for i in range(len(s)):
    if s[i] != character:
        ans += "*"
    else:
        ans += character
print(ans)