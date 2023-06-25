y = int(input())
ans = "NO"
if y%400 == 0:
    ans = "YES"
else:
    if y%100 == 0:
        ans = "NO"
    else:
        if y%4 == 0:
            ans = "YES"
print(ans)