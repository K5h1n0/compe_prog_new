s = input()
ans = ""
a = set("a i u e o".split())
for i in range(len(s)):
    if s[i] not in a:
        ans += s[i]
print(ans)