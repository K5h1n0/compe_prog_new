#解説AC
#このアルゴリズムすごい
n = int(input())
a = list(map(int,input().split()))
suma = sum(a)
if suma % n != 0:
    print(-1)
    exit()
perone = suma//n
ans = 0
for i in range(1,len(a)):
    leftsum = sum(a[:i])
    rightsum = sum(a[i:])
    if i*perone != leftsum:
        ans += 1
    #print(i,"より左に必要なのは",perone,"=",i*perone)
    #print(i,"より右に必要なのは",perone,"=",(len(a)-i)*perone)
    #print("i",i,"番目より左は",leftsum)
    #print("i",i,"番目より右は",rightsum)
print(ans)