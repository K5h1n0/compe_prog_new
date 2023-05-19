from collections import defaultdict

n = int(input())
d = defaultdict(int)
for __ in range(n):
    tmp = input()
    if tmp[0] == "M" or tmp[0] == "A" or tmp[0] == "R" or tmp[0] == "C" or tmp[0] == "H":
        d[tmp[0]] += 1
ans = 0
d = sorted(d.items())
length = len(d)
if length < 3:
    pass
else:
    for i in range(length-2):
        for j in range(i+1,length-1):
            for k in range(j+1,length):
                ans += d[i][1] * d[j][1] * d[k][1]
print(ans)