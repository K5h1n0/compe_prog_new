s = input()
ans = s
if len(s) <= 3:
    pass
else:
    ans = s[:3] + "0" * (len(s)-len(s[:3]))
print(ans)