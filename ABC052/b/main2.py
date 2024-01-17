n = int(input())
s = input()
now = 0
ans = 0
for i in range(len(s)):
    if s[i] == "I":
        now += 1
    elif s[i] == "D":
        now -= 1
    ans = max(ans,now)
print(ans)