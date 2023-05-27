k = int(input())
s = bin(k)[2:]
ans = ""
for i in range(len(s)):
    if s[i] == "1":
        ans += "2"
    else:
        ans += "0"
print(ans)