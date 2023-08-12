n = int(input())
c = []
a = []
for i in range(n):
    c_int = int(input())
    a_list = list(map(int,input().split()))
    c.append((c_int,i))
    a.append(set(a_list))
x = int(input())
c.sort()
ans = []
now = c[i][0]
flag = 0
for i in range(n):
    if flag == 1 and c[i][0] != now:
        break
    elif flag == 1 and c[i][0] == now:
        if x in a[c[i][1]]:
            ans.append(c[i][1]+1)
    elif flag == 0:
        if x in a[c[i][1]]:
            ans.append(c[i][1]+1)
            flag = 1
    now = c[i][0]
ans.sort()
print(len(ans))
print(*ans)