n,k = map(int,input().split())
h = sorted([int(input()) for i in range(n)])
minimum = 10**10
for i in range(n-k+1):
    minimum = min(minimum,h[i+k-1] - h[i])
print(minimum)