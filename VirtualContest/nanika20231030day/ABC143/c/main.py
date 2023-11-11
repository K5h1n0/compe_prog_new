n = int(input())
s = input()
now = "."
ans = 0
for i in range(n):
    if s[i] != now:
        ans += 1
        now = s[i]
print(ans)