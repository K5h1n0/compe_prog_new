s = list(input())
ans = []
for i in range(len(s)):
    if s[i] == "0":
        ans.append("0")
    elif s[i] == "1":
        ans.append("1")
    elif s[i] == "B" and 1 <= len(ans):
        ans = ans[:-1]
print("".join(ans))
