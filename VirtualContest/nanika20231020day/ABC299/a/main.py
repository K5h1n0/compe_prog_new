n = int(input())
s = input()
ans = ""
for i in range(n):
    if s[i] == "|" or s[i] == "*":
        ans += s[i]
if ans == "|*|":
    print("in")
else:
    print("out")