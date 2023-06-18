n = int(input())
s = input()
ans = ""
for i in range(len(s)):
    ans += s[i] + s[i]
print(ans)