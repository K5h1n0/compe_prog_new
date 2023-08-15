n,d = map(int,input().split())
l = []
for i in range(n):
    l.append(input())
maximum = 0
now = 0
for i in range(d):
    flag = True
    for j in range(n):
        flag &= l[j][i] == "o" #この書き方良い
    if flag:
        now += 1
    else:
        now = 0
    maximum = max(maximum,now)
print(maximum)