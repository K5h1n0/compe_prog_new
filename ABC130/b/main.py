n,x = map(int,input().split())
l = list(map(int,input().split()))
accum = [0]
now = 0
for i in range(n):
    now += l[i]
    accum.append(now)
for i in  range(len(accum)):
    if x == accum[i]:
        print(i+1)
        exit()
    elif x < accum[i]:
        print(i)
        exit()