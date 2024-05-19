from collections import deque

n = int(input())
a = list(map(int,input().split()))
d = deque()
d.append(a[0])
for i in range(1,n):
    d.append(a[i])
    one = d.pop()
    two = d.pop()
    flg = 1
    while one == two:
        d.append(one+1)
        if len(d) == 1:
            flg = 0
            break
        one = d.pop()
        two = d.pop()
    if flg:
        d.append(two)
        d.append(one)
print(len(d))