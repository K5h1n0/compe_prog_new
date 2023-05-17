#解説AC

n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(-100,101):
    ans = 0
    for j in range(len(a)):
        ans += (a[j] - i)**2
    l.append(ans)
print(min(l))