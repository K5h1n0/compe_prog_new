from collections import deque

def search(y,x,now,dir):
    global l,snuke,y8,x8,h,w,ans,tmp
    if 0 <= y < h and 0 <= x < w and l[y][x] == snuke[now]:
        if snuke[now] == "e" and now == 4:
            tmp = list(ans)
            return
        nexty = y+y8[dir]
        nextx = x+x8[dir]
        ans.append([nexty,nextx])
        search(nexty,nextx,now+1,dir)
        ans.pop()


h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
ans = deque()
tmp = []
snuke = "snuke"
y8 = [-1,-1,0,1,1,1,0,-1]
x8 = [0,1,1,1,0,-1,-1,-1]
for i in range(h):
    for j in range(w):
        if l[i][j] == "s":
            ans.append([i,j])
            for k in range(8):
                nexty = i+y8[k]
                nextx = j+x8[k]
                if 0 <= nexty < h and 0 <= nextx < w and l[nexty][nextx] == "n":
                    ans.append([nexty,nextx])
                    search(nexty,nextx,1,k)
                    ans.pop()
                    if len(tmp) == 5:
                        for i in range(len(tmp)):
                            print(tmp[i][0]+1,tmp[i][1]+1)
                        exit()
            ans.pop()