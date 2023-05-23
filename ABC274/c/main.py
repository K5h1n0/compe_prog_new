n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(1,len(a)+1):
    l.append(i*2)
    l.append(i*2+1)
print(l)