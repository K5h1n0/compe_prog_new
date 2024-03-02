s = list(input())
s = s[::-1]
ans = []
for i in range(len(s)):
    if s[i] != ".":
        ans.append(s[i])
    else:
        break
ans.reverse()
print("".join(ans))