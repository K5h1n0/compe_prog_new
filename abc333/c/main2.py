n = int(input())
l = [1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111,111111111111,1111111111111]
le = len(l)
ans = []
for i in range(le):
    for j in range(le):
        for k in range(le):
            ans.append(l[i]+l[j]+l[k])
ans = sorted(list(set(ans)))
print(ans[n-1])