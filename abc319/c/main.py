import itertools
import math

l = []
for i in range(3):
    tmp = list(map(int, input().split()))
    l += tmp
cnt = 0
for p in itertools.permutations(range(9)):
    s012 = set()
    s345 = set()
    s678 = set()
    s036 = set()
    s147 = set()
    s258 = set()
    s246 = set()
    s048 = set()
    print(p)
    for i in p:
        d = l[i]
        if i == 0:
            if d in s012:cnt += 1
            s012.add(d)
            if d in s036:cnt += 1
            s036.add(d)
            if d in s048:cnt += 1
            s048.add(d)
        if i == 1:
            if d in s012:cnt += 1
            s012.add(d)
            if d in s147:cnt += 1
            s147.add(d)
        if i == 2:
            if d in s012:cnt += 1
            s012.add(d)
            if d in s258:cnt += 1
            s258.add(d)
            if d in s246:cnt += 1
            s246.add(d)
        if i == 3:
            if d in s345:cnt += 1
            s345.add(d)
            if d in s036:cnt += 1
            s036.add(d)
        if i == 4:
            if d in s345:cnt += 1
            s345.add(d)
            if d in s147:cnt += 1
            s147.add(d)
            if d in s246:cnt += 1
            s246.add(d)
            if d in s048:cnt += 1
            s048.add(d)
        if i == 5:
            if d in s345:cnt += 1
            s345.add(d)
            if d in s258:cnt += 1
            s258.add(d)
        if i == 6:
            if d in s678:cnt += 1
            s678.add(d)
            if d in s036:cnt += 1
            s036.add(d)
            if d in s246:cnt += 1
            s246.add(d)
        if i == 7:
            if d in s678:cnt += 1
            s678.add(d)
            if d in s147:cnt += 1
            s147.add(d)
        if i == 8:
            if d in s678:cnt += 1
            s678.add(d)
            if d in s258:cnt += 1
            s258.add(d)
            if d in s048:cnt += 1
            s048.add(d)
print(cnt/math.factorial(9))