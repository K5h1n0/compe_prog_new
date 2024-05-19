n = int(input())
l = []
total = 0
for i in range(n):
    s,c = input().split()
    total += int(c)
    l.append(s)
l.sort()
print(l[total%n])