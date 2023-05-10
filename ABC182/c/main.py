n = list(input())
ans = 20
for i in range(2**len(n)):
    now = []
    for j in range(len(n)):
        if i >> j & 1:
            now.append(int(n[j]))
    if len(now) == 0 or sum(now) == 0:
        continue
    if sum(now)%3 == 0:
        ans = min(ans,len(n)-len(now))
if ans == 20:
    print(-1)
else:
    print(ans)