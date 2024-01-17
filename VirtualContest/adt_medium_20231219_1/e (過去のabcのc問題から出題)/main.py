n = int(input())
l = []
for i in range(n):
    f,s = map(int,input().split())
    l.append([s,f])
l.sort(reverse=True)
ans = []
maximum = l[0][0]
maxf = l[0][1]
for i in range(1,len(l)):
    if maxf == l[i][1]:
        ans.append(maximum + l[i][0]//2)
    else:
        ans.append(maximum+l[i][0])
print(max(ans))