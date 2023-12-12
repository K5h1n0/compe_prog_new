n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in list(input())])

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

ans = []
for i in range(n):
    for j in range(n):
        for k in range(8):
            nownum = 0
            for m in range(n):
                nowi = (i+dy[k]*m)%n
                nowj = (j+dx[k]*m)%n
                nownum *= 10
                nownum += l[nowi][nowj]
            ans.append(nownum)
print(max(ans))