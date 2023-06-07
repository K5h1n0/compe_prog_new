l1 = []
l2 = []
for _ in range(5):
    s = int(input())
    tmp = s
    s = list(str(s))
    s.reverse()
    s = "".join(s)
    if tmp%10 == 0:
        l2.append([s,tmp])
    else:
        l1.append([s,tmp])
l1.sort(reverse=True)
l3 = l2+l1
ans = 0
for i in range(len(l3)-1):
    if l3[i][1] % 10 == 0:
        ans += l3[i][1]
    else:
        ans += (l3[i][1]//10+1)*10
ans += l3[-1][1]
print(ans)