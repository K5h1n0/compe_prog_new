A,B,a,b = map(int,input().split())
for i in range(10**9):
    if i%A == a and i%B == b:
        print(i)
        exit()