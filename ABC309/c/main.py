n,k = map(int,input().split())
inp = []
total = 0
for i in range(n):
    a,b = map(int,input().split())
    inp.append([a,b])
    total += b
inp.sort()
l = [total]
for i in inp:
    l.append(-i[1])
for i in range(1,len(l)):
    l[i] += l[i-1]
for i in range(len(l)):
    if l[i] <= k:
        print(inp[i][0])
        exit()