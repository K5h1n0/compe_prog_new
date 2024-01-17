s = input()
b = 9999999
e = 0
for i in range(len(s)):
    if s[i] == "A":
        b = min(b,i)
    elif s[i] == "Z":
        e = max(e,i)
print(e-b+1)