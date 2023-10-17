n,m = map(int,input().split())
tmp = -1
for i in range(1,n+1):
    if m < i*i:
        tmp = i
print(tmp*tmp)
print(tmp)