n = int(input())
s = input()
k = int(input())
tmp = s[k-1]
ans = ""
for i in range(len(s)):
    if s[i] == tmp:
        ans += tmp
    else:
        ans += "*"
print(ans)