from collections import deque,defaultdict

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            starti = i
            startj= j
            break
    else:
        continue
    break
q = deque()
q.append((starti,startj))
checked = [[0]*w for _ in range(h)]
y = [-1,0,1,0]
x = [0,1,0,-1]
s = set()
while q:
    nowi,nowj = q.popleft()
    for i in range(4):
        nexti = nowi+y[i]
        nextj = nowj+x[i]
        if 0 <= nexti < h and 0 <= nextj < w and checked[nexti][nextj] == 0 and l[nexti][nextj] == "#":
            checked[nexti][nextj] = 1
            s.add((nexti,nextj))
            q.append((nexti,nextj))
l2 = list(s)
di = defaultdict(int)
dj = defaultdict(int)
for i,j in l2:
    di[i] += 1
    dj[j] += 1
mini = 10**5
minj = 10**5
for i,v in di.items():
    if v < mini:
        mini = v
        ansi = i
for i,v in dj.items():
    if v < minj:
        minj = v
        ansj = i
print(ansi+1,ansj+1)