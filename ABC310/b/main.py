n,m = map(int,input().split())
l = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    l.append([tmp[0],set(tmp[2:])])
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if l[j][0] <= l[i][0] and l[j][1] >= l[i][1] and (l[i][0] > l[j][0] or len(l[i][1]) < len(l[j][1])):
            print("Yes")
            exit()
print("No")
