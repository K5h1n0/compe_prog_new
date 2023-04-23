l = list(map(int,input().split()))
k = int(input())
ans = "No"
for i in range(k):
    if l[0] < l[1] < l[2]:
        ans = "Yes"
        break
    if l[0] >= l[1]:
        l[1] *= 2
    elif l[1] >= l[2]:
        l[2] *= 2
if l[0] < l[1] < l[2]:
    ans = "Yes"
print(ans)