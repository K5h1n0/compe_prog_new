n,m = map(int,input().split())
s = input()
t = input()
ans = 0
flg = True
for i in range(len(s)):
    flg &= s[i] == t[i]
if not flg:
    ans += 2
flg = True
for i in range(len(s)):
    flg &= s[i] == t[len(t)-len(s)+i]
if not flg:
    ans += 1
print(ans)