n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
l = []
for i in range(len(x)-1):
    l.append(abs(x[i]-x[i+1]))
l.sort(reverse=True)
l = l[n-1:]
print(sum(l))