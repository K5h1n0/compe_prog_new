from collections import defaultdict

n = int(input())
l = []
d = defaultdict(list)
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
s = list(input())
for i in range(len(l)):
    d[l[i][1]].append([l[i][0],s[i]])
ans = "No"
for i in d:
    maximum = 0
    minimum = 1 << 60
    for j in d[i]:
        if j[1] == "R":
            minimum = min(minimum,j[0])            
        elif j[1] == "L":
            maximum = max(maximum,j[0])
    if minimum <= maximum:
        ans = "Yes"
        print(ans)
        exit()
print(ans)