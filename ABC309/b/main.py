import copy

n = int(input())
l1 = []
for i in range(n):
    l1.append(list(input()))
l2 = copy.deepcopy(l1)

for i in range(n-1):
    l2[0][i+1] = l1[0][i]
for i in range(n-1):
    l2[i+1][n-1] = l1[i][n-1]
for i in range(n-1,0,-1):
    l2[n-1][i-1] = l1[n-1][i]
for i in range(n-1,0,-1):
    l2[i-1][0] = l1[i][0]
for i in range(n):
    print(*l2[i],sep="")