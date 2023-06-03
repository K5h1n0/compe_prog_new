n = int(input())
l = []
l2 = []
minimum = 10**10
for i in range(n):
    s,a = input().split()
    minimum = min(minimum,int(a))
    l.append(s)
    l2.append(int(a))
index = l2.index(minimum)
for i in range(n):
    print(l[(i+index)%n])