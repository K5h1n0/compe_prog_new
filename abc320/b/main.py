s = list(input())
ans = 0
tmp = s[::-1]
if s == tmp:
    print(len(s))
    exit()
for i in range(0, len(s)-1):
    for j in range(i+1, len(s)):
        tmp = s[i:j]
        tmp2 = s[i:j][::-1]
        if tmp == tmp2:
            ans = max(len(tmp), ans)
print(ans)
