n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
total = 0
for i in range(n):
    if l[i][1] < m:
        m -= l[i][1]
        total += l[i][0]*l[i][1]
    else:
        index = i
        break
total += m*l[index][0]
print(total)