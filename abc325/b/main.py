n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
maximum = 0
for i in range(24):
    now = 0
    for j in range(len(l)):
        if 9 <= (i + l[j][1])%24 <18:
            now += l[j][0]
    maximum = max(maximum,now)
print(maximum)