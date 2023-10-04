n,m,p = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
total = 0
for i in range(n):
    if p <= a[i]:
        total += p*m
        continue
    for j in range(m):
        now_combi = a[i]+b[j]
        if now_combi < p:
            total += now_combi
        else:
            total += p*(m-j)
            break
print(total)