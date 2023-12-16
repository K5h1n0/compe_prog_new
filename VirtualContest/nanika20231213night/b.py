s = input()
t = input()
for i in range(26):
    now = []
    for j in range(len(s)):
        now.append(chr((ord(s[j])-ord("a")+i)%26+ord("a")))
    if "".join(now) == t:
        print("Yes")
        exit()
print("No")