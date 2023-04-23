n = int(input())
p = list(map(int,input().split()))
u = []
tmp = p[-1]
for i in range(len(p)-1,-1,-1):
    if p[i] <= tmp:
        u.append(p[i])
        tmp = p[i]
    else:
        p[i] -= 1
        for j in range(len(u)):
            if p[i] == u[j]:
                u[j] += 1
        break
p = p[:i+1]
u.sort(reverse=True)
p = p + u
print(*p)