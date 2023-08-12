n,k = map(int,input().split())
a = list(map(int,input().split()))
seta = set(a)
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
ans = []
for i in a:
    minimum = 10**10
    for j in range(len(l)):
        if j+1 in seta:
            continue
        distance = ((l[i-1][0] - l[j][0])**2 + (l[i-1][1] - l[j][1])**2) ** 0.5
        minimum = min(minimum,distance)
    ans.append(minimum)
print(max(ans))