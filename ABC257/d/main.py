from collections import deque

n = int(input())
l = []
for i in range(n):
    x,y,p = map(int,input().split())
    l.append([x,y,p])

def bfs(start,s):
    visited = [0]*n
    q = deque()
    q.append((l[start][0],l[start][1],l[start][2]))
    visited[start] = 1
    while q:
        nowx,nowy,nowp = q.popleft()
        for i in range(n): # 全頂点見る
            nowd = abs(nowx-l[i][0])+abs(nowy-l[i][1])
            if visited[i] == 0 and nowd <= nowp*s:
                visited[i] = 1
                q.append((l[i][0],l[i][1],l[i][2]))
    return all(visited)

lefts = -1
rights = 10**10
while 1 < rights - lefts:
    nows = (rights+lefts)//2
    flg = False
    for i in range(n):
        if bfs(i,nows):
            flg = True
            #1個でも全頂点にたどり着けたら、それ以降、他の点でBFSを行う必要がない。
            break
    if flg:
        rights = nows
    else:
        lefts = nows
print(rights)