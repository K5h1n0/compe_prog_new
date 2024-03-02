n = int(input())
l = []
for i in range(10000000):
    if 10**18 < i*i*i:
        break
    now = str(i*i*i)
    length = len(now)
    for j in range(len(now)//2+1):
        if now[j] != now[length-j-1]:
            break
    else:
        l.append(i*i*i)
for i in range(len(l)-1,-1,-1):
    if l[i] <= n:
        print(l[i])
        break