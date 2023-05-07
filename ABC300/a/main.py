n,a,b = map(int,input().split())
l = list(map(int,input().split()))
for i in range(len(l)):
    if a + b == l[i]:
        print(i+1)
        exit()