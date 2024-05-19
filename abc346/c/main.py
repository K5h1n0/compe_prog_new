n,k = map(int,input().split())
a = list(map(int,input().split()))
sum = (k * (k+1))//2
num_set = set()
for i in range(len(a)):
    if a[i] <= k and a[i] not in num_set:
        sum -= a[i]
        num_set.add(a[i])
print(sum)