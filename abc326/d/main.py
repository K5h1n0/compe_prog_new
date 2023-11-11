import itertools

n = int(input())
r = input()
c = input()
l = ["###..",
     "##.#.",
     "#.#.#",
     ".#.##",
     "..###"]
abc = [list("ABC"),list("ACB"),list("BAC"),list("BCA"),list("CAB"),list("CBA")]
cnt = 0
for v in itertools.permutations(range(5)):
    for i1 in abc:
        for i2 in abc:
            for i3 in abc:
                for i4 in abc:
                    for i5 in abc:
                            now = []
                            now.append(l[v[0]].replace("#",i1[0],1).replace("#",i1[1],1).replace("#",i1[2],1))
                            now.append(l[v[1]].replace("#",i2[0],1).replace("#",i2[1],1).replace("#",i2[2],1))
                            now.append(l[v[2]].replace("#",i3[0],1).replace("#",i3[1],1).replace("#",i3[2],1))
                            now.append(l[v[3]].replace("#",i4[0],1).replace("#",i4[1],1).replace("#",i4[2],1))
                            now.append(l[v[4]].replace("#",i5[0],1).replace("#",i5[1],1).replace("#",i5[2],1))
                            
                            left = list("#####")
                            left[v[0]] = i1[0]
                            left[v[1]] = i2[0]
                            left[v[2]] = i3[0]
                            left[v[3]] = i4[0]
                            left[v[4]] = i5[0]

                            r = list("#####")
                            r[v[4]] = i5[2]
                            r[v[3]] = i4[2]
                            r[v[2]] = i3[2]
                            r[v[1]] = i2[2]
                            r[v[0]] = i1[2]

                            cnt += 1
print(cnt)