n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
l.sort()
number = l[0][0] + l[-1][0] - l[0][0] + l[-1][1]
print(number)