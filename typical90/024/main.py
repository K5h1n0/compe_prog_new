n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
total = 0
for i in range(n):
    total += abs(a[i]-b[i])
if total <= k and total%2 == k%2:
    print("Yes")
else:
    print("No")