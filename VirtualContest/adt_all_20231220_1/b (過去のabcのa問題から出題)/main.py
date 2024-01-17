s = list(map(int,input().split()))
s2 = sorted(s[:])
flg = True
for i in range(8):
    flg &= s[i] == s2[i] and 100 <= s2[i] <= 675 and s2[i]%25 == 0
if flg:
    print("Yes")
else:
    print("No")