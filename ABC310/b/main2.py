n,m = map(int,input().split())
p = []
f = []
for i in range(n):
    tmp = list(map(int,input().split()))
    p.append(tmp[0])
    f.append(set(tmp[2:]))
flag = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        flag |= p[j] <= p[i] and f[j] >= f[i] and ( p[j] < p[i] or len(f[j]) > len(f[i]))
print("Yes" if flag else "No")