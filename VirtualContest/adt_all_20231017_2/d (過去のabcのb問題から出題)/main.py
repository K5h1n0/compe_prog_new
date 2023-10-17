n,a,b = map(int,input().split())
ans = []
for i in range(n):
    if i%2 == 0:
        now = ""
        for j in range(n):
            if j % 2:
                now += "#"*b
            else:
                now += "."*b
        for j in range(a):
            ans.append(now)
    elif i%2 == 1:
        now = ""
        for j in range(n):
            if j % 2:
                now += "."*b
            else:
                now += "#"*b
        for j in range(a):
            ans.append(now)
print(*ans,sep="\n")