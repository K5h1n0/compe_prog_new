n,x = map(int,input().split())
length = 100001
l1 = [0]*length
l2 = [0]*length
for i in range(n):
    a,b = map(int,input().split())
    if i % 2:
        l2 = [0]*length
        for j in range(length):
            if l1[j] == 1:
                l2[j+a] = 1
                l2[j+b] = 1    
    else:
        if i == 0:
            l1[a] = 1
            l1[b] = 1
            continue
        l1 = [0]*length
        for j in range(length):
            if l2[j] == 1:
                l1[j+a] = 1
                l1[j+b] = 1
if n%2 and l1[x]:
    print("Yes")
elif n%2 == 0 and l2[x]:
    print("Yes")
else:
    print("No")