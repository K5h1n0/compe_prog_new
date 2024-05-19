n = int(input())
h = list(map(int,input().split()))
now = h[0]
for i in range(1,n):
    if h[i] > now:
        now = h[i]
        print(i+1)
        exit()
print(-1)