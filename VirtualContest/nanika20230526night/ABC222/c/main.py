from collections import defaultdict

n,m = map(int,input().split())
a = []
for i in range(n*2):
    a.append(list(input()))
l = [0]*2*n
d = defaultdict(int)
for i in range(m):
    for j in range(n):
        w = 2*j
        if a[w][i] == "G" and a[w+1][i] == "C" or a[w][i] == "C" and a[w+1][i] == "P" or a[w][i] == "P" and a[w+1][i] == "G":
            d[w+1] += 1
        elif a[w+1][i] == "G" and a[w][i] == "C" or a[w+1][i] == "C" and a[w][i] == "P" or a[w+1][i] == "P" and a[w][i] == "G":
            d[w+1+1] += 1
    break
    
print(d)