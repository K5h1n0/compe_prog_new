n,p,q = map(int,input().split())
l = list(map(int,input().split()))
minimum = 999999
for i in range(n):
    minimum = min(minimum,l[i] + q)
print(min(p,minimum))