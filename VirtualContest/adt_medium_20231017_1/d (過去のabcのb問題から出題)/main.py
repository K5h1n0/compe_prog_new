n,m = map(int,input().split())
pair = set()
for i in range(1,n+1):
    for j in range(i+1,n+1):
        pair.add((i,j))

ansset = set()
for i in range(m):
    k,*arg = map(int,input().split())
    for j in range(k):
        for m in range(j+1,k):
            if (arg[j],arg[m]) in pair:
                ansset.add((arg[j],arg[m]))                                
if len(pair) == len(ansset):
    print("Yes")
else:
    print("No")