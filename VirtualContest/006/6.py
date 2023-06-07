n = int(input())
l = []
length = []
for i in range(n):
    a,b = map(int,input().split())
    l.append(b)
    length.append(a*b)
print(sum(length)/sum(l))