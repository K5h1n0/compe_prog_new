from itertools import permutations

n, m = map(int,input().split())
s = []
strlen = 0
for _ in range(n):
    inp = input()
    s.append(inp)
    strlen += len(inp)
sett = set()
for _ in range(m):
    sett.add(input())
print(s)
print(sett)
print(strlen)
for i in permutations(s,n):
    print(i)

for i in range(2**(16-strlen)):
    print(i)        