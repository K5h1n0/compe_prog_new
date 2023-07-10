n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    success = a*10**100//(a+b)
    l.append((success,i))
l.sort(reverse=True)
ans = []
tmp_l = [l[0][1]+1]
tmp_v = l[0][0]
for i in range(1,len(l)):
    if tmp_v == l[i][0]:
        tmp_l.append(l[i][1]+1)
    else:
        tmp_l.sort()
        ans += tmp_l
        tmp_l = []
        tmp_l.append(l[i][1]+1)
        tmp_v = l[i][0]
tmp_l.sort()
ans += tmp_l
print(*ans)
