h,w = map(int,input().split())
l1 = []
for i in range(h):
    l1.append(list(input()))
l2 = []
for i in range(h):
    l2.append(list(input()))
l1 = list(map(list,zip(*l1)))
l2 = list(map(list,zip(*l2)))
l1.sort()
l2.sort()
if l1 == l2:
    print("Yes")
else:
    print("No")