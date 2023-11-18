n,x = map(int,input().split())
l = list(map(int,input().split()))
sum = 0
for i in range(n):
    if l[i] <= x:
        sum += l[i]
print(sum)