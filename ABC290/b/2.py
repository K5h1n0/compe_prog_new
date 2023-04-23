n,k = map(int,input().split())
s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "x":
        ans += "x"
        pass
    elif s[i] == "o" and 0 < k:
        ans += "o"
        k -= 1
    else:
        ans += "x"
print(ans)