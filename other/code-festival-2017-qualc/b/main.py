n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(n):
    if a[i]%2 == 0:
        l.append([0,0,1])
    else:
        l.append([0,1,1])

ans = 0
l2 = []
def f(x,y,cnt):
    global ans
    if cnt == len(l):
        if 1 in l2:
            ans += 1
        return
    for i in range(3):
        l2.append(l[cnt][i])
        f(x,y,cnt+1)
        l2.pop()

f(0,0,0)
print(ans)