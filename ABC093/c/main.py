l = list(map(int,input().split()))
cnt = 0
while min(l) != max(l):
    if 2 < max(l) - min(l):
        l[l.index(min(l))] += 2
    else:
        l[l.index(min(l))] += 1
        l[l.index(min(l))] += 1
    cnt += 1
print(cnt)