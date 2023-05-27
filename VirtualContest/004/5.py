x,y = map(int,input().split())
ans = x
for i in range(1,10**5):
    if ans * i % y != 0:
        print(ans*i)
        exit()
print(-1)