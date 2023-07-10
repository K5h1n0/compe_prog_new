s = list(map(int,input().split()))
if 100 <= s[0] <= 675 and s[0] % 25 == 0:
    pass
else:
    print("No")
    exit()
for i in range(1,len(s)):
    if s[i-1] <= s[i] and 100 <= s[i] <= 675 and s[i]%25 == 0:
        pass
    else:
        print("No")
        exit()
print("Yes")