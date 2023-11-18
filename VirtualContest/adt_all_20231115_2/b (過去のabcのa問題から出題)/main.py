n = int(input())
s = list(input())
t = list(input())
for i in range(n):
    if s[i] == "1":
        s[i] = "l"
    if t[i] == "1":
        t[i] = "l"
    if s[i] == "0":
        s[i] = "o"
    if t[i] == "0":
        t[i] = "o"
if s == t:
    print("Yes")
else:
    print("No")