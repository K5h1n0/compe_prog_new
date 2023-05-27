n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
maximum = 0
for i in range(n-1):
    for j in range(i+1,n):
        maximum = max(maximum,((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)**0.5)
print(maximum)