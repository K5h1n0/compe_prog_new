n = int(input())
a = list(map(int,input().split()))
l = [0,0,0]
for i in a:
    if i % 4 == 0:
        l[2] += 1
    elif i % 2 == 0:
        l[1] += 1
    else:
        l[0] += 1
ans = "Yes"
if l[2] < l[0]:
    if l[0] - l[2] == 1 and l[1] != 0:
        ans = "No"
    elif 1 < l[0] - l[2]:
        ans = "No"
print(ans)