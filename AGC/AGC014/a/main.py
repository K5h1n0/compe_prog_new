import copy

l = list(map(int,input().split()))
l2 = copy.copy(l)
ans = 0
hantei = [l[0]%2,l[1]%2,l[2]%2]
while 1 not in hantei:
    l2[0] = (l[1]+l[2])//2
    l2[1] = (l[0]+l[2])//2
    l2[2] = (l[0]+l[1])//2
    if l == l2:
        print(-1)
        exit()
    l = copy.copy(l2)
    hantei = [l[0]%2,l[1]%2,l[2]%2]
    ans += 1
print(ans)