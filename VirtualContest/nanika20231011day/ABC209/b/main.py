n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if i%2:
        x -= a[i]
        x += 1
    else:
        x -= a[i]
    if x < 0:
        print("No")
        exit()
print("Yes")