n = int(input())
ans = 0
if 1000 <= n <= 999999:
    ans += n-999
if 1000000 <= n <= 999999999:
    ans += (n-999999)*2 + 999000
if 1000000000 <= n <= 999999999999:
    ans += (n-999999999)*3 + 1998999000
if 1000000000000 <= n <= 999999999999999:
    ans += (n-999999999999)*4 + 2998998999000
if 1000000000000000 <= n:
    ans += (n-999999999999999)*5 + 3998998998999000
print(ans)
