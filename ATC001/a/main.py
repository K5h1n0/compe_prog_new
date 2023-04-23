import sys
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())
l = []
for i in range(h):
    row = list(input())
    for j in range(len(row)):
        if row[j] == "s":
            starty = i
            startx = j
        elif row[j] == "g":
            goaly = i
            goalx = j
    l.append(row)
#print(starty,startx)
#print(goaly,goalx)
#print(*l,sep="\n")

y = [-1,0,1,0]
x = [0,1,0,-1]

searched = [[0 for i in range(w)]for i in range(h)]
#print(*searched,sep="\n")

def dfs(nowy,nowx):
    #print(nowy,nowx)
    if nowy == goaly and nowx == goalx:
        print("Yes")
        exit()
    for i in range(4):
        nexty = nowy + y[i]
        nextx = nowx + x[i]
        # print("nexty",nexty,"nextx",nextx)
        if (0 <= nexty < h) and (0 <= nextx < w) and l[nexty][nextx] != "#" and searched[nexty][nextx] == 0:
            searched[nexty][nextx] = 1
            dfs(nexty,nextx)

searched[starty][startx] = 1
dfs(starty,startx)
#print(*searched,sep="\n")
print("No")