s = list(input())
ans = 45
for i in range(len(s)):
    ans -= int(s[i])
print(ans)