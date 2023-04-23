import sys
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())
l = []
for i in range(h):
    tmp = list(map(int,input().split()))
    l.append(tmp)

ans = 0
now = []

def f(y,x):
    now.append(l[y][x])
    if y == h-1 and x == w-1:
        length = len(now)
        if length == len(set(now)):
            global ans
            ans += 1
    for i in range(2):
        if i == 0:
            if x+1 < w:
                f(y,x+1)
                now.pop()
        elif i == 1:
            if y+1 < h:
                f(y+1,x)
                now.pop()

f(0,0)
print(ans)