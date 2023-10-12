n = int(input())
lx = []
ly = []
for i in range(n):
    x, y = map(int, input().split())
    lx.append(x)
    ly.append(y)
lx.sort()
ly.sort()
print(lx)
print(ly)
