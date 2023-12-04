import heapq

n,m,l = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a2 = []
b2 = []
for i,v in enumerate(a):
    a2.append((v,i))
for i,v in enumerate(b):
    b2.append((v,i))
a2.sort(reverse=True)
b2.sort(reverse=True)

ngset = set()
for i in range(l):
    c,d = map(int,input().split())
    ngset.add((c-1,d-1))

ans = []
for i in range(len(a2)):
    for j in range(len(b2)):
        if (a2[i][1],b2[j][1]) in ngset:
            continue
        else:
            ans.append(a2[i][0]+b2[j][0])
            break
print(max(ans))