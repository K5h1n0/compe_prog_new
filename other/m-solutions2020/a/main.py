x = int(input())
if 400 <= x <= 599:
    ans = 8
elif x <= 799:
    ans = 7
elif x <= 999:
    ans = 6
elif x <= 1199:
    ans = 5
elif x <= 1399:
    ans = 4
elif x <= 1599:
    ans = 3
elif x <= 1799:
    ans = 2
elif x <= 1999:
    ans = 1
print(ans)