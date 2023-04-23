n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
l1 = []
l2 = []
l3 = []
for i in range(len(p)):
    if p[i] <= a:
        l1.append(p[i])
    elif a+1 <= p[i] <= b:
        l2.append(p[i])
    else:
        l3.append(p[i])
print(min(min(len(l1),len(l2)),len(l3)))