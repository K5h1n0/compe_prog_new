from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    inp = input()
    d[inp] += 1
print(max(d,key=d.get))