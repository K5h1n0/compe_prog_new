n,k = map(int,input().split())
l = [0]*k
for i in range(k):
    l[i] += 1
    n -= 1
l[0] += n
print(max(l)-min(l))