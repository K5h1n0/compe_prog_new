n = int(input())
s = []
for i in range(n):
    s.append(list(input()))
t = []
for i in range(n):
    t.append(list(input()))
print(*s,sep="\n")
print()
print(*t,sep="\n")

def chip(input):
    miny = 300
    minx = 300
    maxy = 0
    maxx = 0
    for i in range(len(input[0])):
        for j in range(len(input[0])):
            if input[i][j] == "#":
                miny = min(miny,i)
                minx = min(minx,j)
                maxy = max(maxy,i)
                maxx = max(maxx,j)
    news = [["."]*(maxx-minx+1) for _ in range(maxy-miny+1)]
    for i in range(maxy-miny+1):
        for j in range(maxx-minx+1):
            news[i][j] = s[miny+i][minx+j]
    return news,miny,minx,maxy,maxx

s1,_,_,_,_ = chip(s)
t,_,_,_,_ = chip(t)

if s1 == t:
    print("Yes")
    exit()

news = []
for x in zip(*s1[::-1]):
    news.append(list(x))
if news == t:
    print("Yes")
    exit()

s1 = news
news = []
for x in zip(*s1[::-1]):
    news.append(list(x))
if news == t:
    print("Yes")
    exit()

s1 = news
news = []
for x in zip(*s1[::-1]):
    news.append(list(x))
if news == t:
    print("Yes")
    exit()

s1 = news
news = []
for x in zip(*s1[::-1]):
    news.append(list(x))
if news == t:
    print("Yes")
    exit()

print("No")