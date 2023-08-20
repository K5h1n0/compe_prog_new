n = int(input())
l = []
for i in range(n):
    f,s = map(int,input().split())
    l.append((s,f)) #逆
l.sort(reverse=True)
ans = []
max1 = l[0]
for i in range(1,len(l)):
    if max1[1] != l[i][1]:
        ans.append(max1[0]+l[i][0])
    else:
        ans.append(max1[0]+(l[i][0]//2))
print(max(ans))