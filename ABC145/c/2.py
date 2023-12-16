import itertools

n = int(input())
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
ans = []
for p in itertools.permutations(range(n)):
    res = 0
    for i in range(1,len(p)):
        res += ((l[p[i-1]][0]-l[p[i]][0])**2 + (l[p[i-1]][1]-l[p[i]][1])**2)**0.5
    ans.append(res)
print(sum(ans)/len(ans))