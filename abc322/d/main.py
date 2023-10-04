l1 = []
l2 = []
l3 = []
set1 = set()
set2 = set()
set3 = set()
for i in range(4):
    inp = list(input())
    for j in range(4):
        if inp[j] == "#":
            set1.add((i, j))
    l1.append(inp)
for i in range(4):
    inp = list(input())
    for j in range(4):
        if inp[j] == "#":
            set2.add((i, j))
    l2.append(inp)
for i in range(4):
    inp = list(input())
    for j in range(4):
        if inp[j] == "#":
            set3.add((i, j))
    l3.append(inp)
# print(*l1, sep="\n")
# print(*l2, sep="\n")
# print(*l3, sep="\n")
# print(set1)
# print(set2)
# print(set3)


def normalize(s):
    newset = set()
    my = min(y for (y, x) in s)
    mx = min(x for (y, x) in s)
    xmax = 0
    ymax = 0
    for (y, x) in s:
        nowy = y-my
        nowx = x-mx
        xmax = max(xmax, nowx)
        ymax = max(ymax, nowy)
        newset.add((nowy, nowx))
    return newset, xmax, ymax


set1, xmax1, ymax1 = normalize(set1)
set2, xmax2, ymax2 = normalize(set2)
set3, xmax3, ymax3 = normalize(set3)
# print(set1, xmax1, ymax1)
# print(set2, xmax2, ymax2)
# print(set3, xmax3, ymax3)

for cnt1 in range(4):
    for i1 in range(4-ymax1):
        for j1 in range(4-xmax1):
            # print(i1, j1)

            for cnt2 in range(4):
                for i2 in range(4-ymax2):
                    for j2 in range(4-xmax2):
                        # print(i2, j2)

                        for cnt3 in range(4):
                            for i3 in range(4-ymax3):
                                for j3 in range(4-xmax3):
                                    # print(i3, j3)

                                    #
                                    hanteiset = set()
                                    flg = True
                                    for y, x in set1:
                                        now = (y+i1, x+j1)
                                        if now in hanteiset:
                                            flg = False
                                        else:
                                            hanteiset.add(now)
                                    for y, x in set2:
                                        now = (y+i2, x+j2)
                                        if now in hanteiset:
                                            flg = False
                                        else:
                                            hanteiset.add(now)
                                    for y, x in set3:
                                        now = (y+i3, x+j3)
                                        if now in hanteiset:
                                            flg = False
                                        else:
                                            hanteiset.add(now)
                                    for i in range(4):
                                        for j in range(4):
                                            flg &= (i, j) in hanteiset
                                    if flg:
                                        print("Yes")
                                        exit()

                            else:
                                newset3 = set()
                                for y, x in set3:
                                    newset3.add((x, 3-y))
                                set3, xmax3, ymax3 = normalize(newset3)
                else:
                    newset2 = set()
                    for y, x in set2:
                        newset2.add((x, 3-y))
                    set2, xmax2, ymax2 = normalize(newset2)
    else:
        newset1 = set()
        for y, x in set1:
            newset1.add((x, 3-y))
            set1, xmax1, ymax1 = normalize(newset1)
print("No")
