import itertools

def fact(x):
    if x == 0: return 1
    else: return x * fact(x-1)

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
tmp = []
for i in itertools.permutations(range(n),n):
    now_route = 0
    for j in range(len(i)-1):
        now_route += (((l[i[j]][0] - l[i[j+1]][0])**2+(l[i[j]][1]-l[i[j+1]][1])**2)**0.5)
    tmp.append(now_route)
print(sum(tmp)/fact(n))