import sys
sys.setrecursionlimit(10**6)

def dfs(nowy,nowx,cnt):
    if l[nowy][nowx] == snuke[cnt]:
        for dy,dx in (-1,0),(0,1),(1,0),(0,-1):
            nexty = nowy+dy
            nextx = nowx+dx
            if nexty == h-1 and nextx == w-1:
                global ans
                ans = "Yes"
                return

            if 0 <= nexty <= h-1 and 0 <= nextx <= w-1:
                if (nexty,nextx) not in set_:
                    set_.add((nexty,nextx))
                    dfs(nexty,nextx,(cnt+1)%5)
                    set_.remove((nexty,nextx))
        

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
snuke = "snuke"
set_ = set()

ans = "No"
if l[0][0] == "s":
    set_.add((0,0))
    dfs(0,0,0)
print(ans)