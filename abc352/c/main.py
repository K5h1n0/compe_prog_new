n = int(input())
l = []
sum = 0
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
    sum += a
maximum = 0
for i in range(n):
    now = sum - l[i][0] + l[i][1]
    maximum = max(maximum,now)
print(maximum)