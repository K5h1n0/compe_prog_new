n,x = map(int,input().split())
a = list(map(int,input().split()))
seta = set(a[:])
for i in range(n):
    if a[i] + x in seta:
        print("Yes")
        exit()
print("No")