n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(n-1):
    s,t = map(int,input().split())
    res = a[i]//s
    a[i+1] += res * t
print(a[-1])