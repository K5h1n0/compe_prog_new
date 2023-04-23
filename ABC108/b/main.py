#自力で解けたけど、よくわからない
x1,y1,x2,y2 = map(int,input().split())
zoukaryox = x1-x2
zoukaryoy = y1-y2
x3 = x2+zoukaryoy
y3 = y2-zoukaryox
print(x3,y3,x3+zoukaryox,y3+zoukaryoy)