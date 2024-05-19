x = int(input())
ans = 0
ans += (x//11)*2
if x%11 == 0:
    pass
elif 7 <= x%11:
    ans += 2
else:
    ans += 1
print(ans)