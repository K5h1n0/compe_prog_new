n = int(input())
l = sorted(list(map(int,input().split())))
if len(l) == 1:
    print("Yes")
    exit()
u = l[(n+2-1)//2:]
d = l[:(n+2-1)//2]
ans = "Yes"
for i in range(len(u)):
    if u[i] <= d[i+1]:
        ans = "No"
        break
print(ans)