n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n):
    if b[i] - a[i] < 0:
        a[i] = 0
        b[i] = b[i] - a[i]
        