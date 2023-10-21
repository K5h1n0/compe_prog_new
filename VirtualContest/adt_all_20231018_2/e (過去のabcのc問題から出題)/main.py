s = input()
if len(set(list(s))) == 1 and "a" in set(s):
    print("Yes")
    exit()
cnt1 = 0
for i in range(len(s)):
    if s[i] == "a":
        cnt1 += 1
    else:
        break
cnt2 = 0
for i in range(len(s)-1,-1,-1):
    if s[i] == "a":
        cnt2 += 1
    else:
        break
print(cnt1)
print(cnt2)
tmp = s[cnt1:-cnt2]
if tmp == tmp[::-1] and cnt1 <= cnt2:
    print("Yes")
else:
    print("No")