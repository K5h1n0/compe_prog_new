n = int(input())
a = list(map(int,input().split()))
now = []
for i,v in enumerate(a):
    now.append([v,i+1])
for i in range(n-1):
    newnow = []
    for j in range(len(now)//2):
        if now[2*j][0] < now[2*j+1][0]:
            newnow.append(now[2*j+1])
        else:
            newnow.append(now[2*j])
    now = newnow[:]
if now[0][0] < now[1][0]:
    print(now[0][1])
else:
    print(now[1][1])