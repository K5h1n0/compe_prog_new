n,k = map(int,input().split())
ans = (n-k)%3
if ans == 0:
    print("Drew")
elif ans == 2:
    print("Won")
else:
    print("Lost")