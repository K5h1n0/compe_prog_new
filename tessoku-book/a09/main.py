#for文の量もうちょっと減らせないか？

h,w,n = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
l2 = []
for i in range(h+1):
    l2.append([0]*(w+1))
for i in range(len(l)):
    i_ul = l[i][0]-1
    j_ul = l[i][1]-1
    i_lr = l[i][2]
    j_lr = l[i][3]
    l2[i_ul][j_ul] += 1
    l2[i_lr][j_lr] += 1
    l2[i_ul][j_lr] -= 1
    l2[i_lr][j_ul] -= 1
for i in range(len(l2)):
    tmp = 0
    for j in range(len(l2[i])):
        tmp += l2[i][j]
        l2[i][j] = tmp
for j in range(len(l2[0])):
    tmp = 0
    for i in range(len(l2)):
        tmp += l2[i][j]
        l2[i][j] = tmp
l2 = l2[:-1]
for i in range(len(l2)):
    l2[i] = l2[i][:-1]
for i in range(len(l2)):
    print(*l2[i])