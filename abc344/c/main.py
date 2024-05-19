n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
l = int(input())
c = list(map(int,input().split()))
q = int(input())
x = list(map(int,input().split()))
numset = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            numset.add(a[i]+b[j]+c[k])
for i in range(q):
    if x[i] in numset:
        print("Yes")
    else:
        print("No")