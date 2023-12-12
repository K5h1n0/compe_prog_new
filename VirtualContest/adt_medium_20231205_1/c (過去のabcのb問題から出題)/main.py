n = int(input())
a = list(map(int,input().split()))
l = []
for i,v in enumerate(a):
    l.append((v,i+1))
print(sorted(l)[-2][1])