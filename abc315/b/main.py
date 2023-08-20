m = int(input())
d = list(map(int,input().split()))
half = (sum(d)+1)//2
for i in range(m):
    for j in range(d[i]):
        half -= 1
        if half == 0:
            print(i+1,j+1)
            exit()