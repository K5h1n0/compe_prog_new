from collections import defaultdict

m = int(input())
l = []
d1 = defaultdict(list)
d2 = defaultdict(list)
d3 = defaultdict(list)
for i in range(3):
    tmp = list(input())
    l.append(tmp)
    for j in range(m):
        if i == 0:
            d1[tmp[j]].append(j)
        elif i == 1:
            d2[tmp[j]].append(j)
        elif i == 2:
            d3[tmp[j]].append(j)
ans = []
for i in range(10):
    selected = set()
    ans1 = -1
    ans2 = -1
    ans3 = -1
    if len(d1[str(i)]) == 0:
        continue
    else:
        ans1 = min(d1[str(i)])
        selected.add(j)

    if len(d2[str(i)]) == 0:
        continue
    for j in d2[str(i)]:
        if j in selected:
            continue
        else:
            ans2 = j
            selected.add(j)
            break
    else:
        ans2 = min(d2[str(i)])+m

    flg = 0
    if len(d3[str(i)]) == 0:
        continue
    for j in d3[str(i)]:
        if j in selected and flg == 0:
            flg = 1
            continue
        elif j not in selected and flg == 0:
            ans3 = j
            selected.add(j)
            break
    else:

        if len(selected) == 1 and flg == 1:
            ans3 = min(d3[str(i)])+m+m
        elif len(selected) == 2:
            ans3 = min(d3[str(i)])+m

    ans.append(max(ans1, max(ans2, ans3)))
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
"""
m = int(input())
l = []
for i in range(3):
    l.append(list(input()))
ans = []
for i in range(10):
    selected = set()
    ans1 = -1
    ans2 = -1
    ans3 = -1
    for j in range(m):
        if l[0][j] == str(i):
            selected.add(j)
            ans1 = j
            break
    else:
        if ans1 == -1:
            continue
    memory = -1
    memory_list = []
    for j in range(m):
        if l[1][j] == str(i):
            if j in selected:
                memory = j
                continue
            else:
                selected.add(j)
                ans2 = j
                break
    else:
        if ans2 == -1 and memory == -1:
            continue
        elif ans2 == -1:
            ans2 = memory + m
    memory_list = []
    for j in range(m):
        if l[2][j] == str(i):
            if j in selected:
                memory_list.append(j)
                continue
            else:
                selected.add(j)
                ans3 = j
                break
    else:
        if ans3 == -1 and len(memory_list) == 0:
            continue
        elif ans3 == -1:
            ans3 = min(memory_list)+m
    ans.append(max(ans1, max(ans2, ans3)))
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
"""
