s = list(input())
ans = 0
now = s[0]
for i in range(1,len(s)):
    if now != s[i]:
        ans += 1
        now = s[i]
print(ans)