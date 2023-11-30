s = input()
ans = ""
for i in s:
    if ord("A") <= ord(i) <= ord("Z"):
        ans += chr(ord(i)+32)
    else:
        ans += chr(ord(i)-32)
print(ans)