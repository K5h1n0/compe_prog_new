n = int(input())
ans = []
for i in range(n+1):
    l = []
    for j in range(1, 10):
        if n % j == 0 and i % (n/j) == 0:
            l.append(j)
    if len(l) == 0:
        ans.append("-")
    else:
        ans.append(str(min(l)))
print("".join(ans))
