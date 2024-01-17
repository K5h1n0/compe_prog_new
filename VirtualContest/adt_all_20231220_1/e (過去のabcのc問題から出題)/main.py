n = list(input())
n.sort(reverse=True)
ans = 0
for i in range(2**len(n)):
    now1 = []
    now2 = []
    for j in range(len(n)):
        if (i >> j) & 1:
            now1.append(n[j])
        else:
            now2.append(n[j])
    if len(now1) == 0 or len(now2) == 0:
        continue
    ans = max(ans,int("".join(now1))*int("".join(now2)))
print(ans)