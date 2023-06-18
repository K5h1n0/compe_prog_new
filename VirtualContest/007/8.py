n = int(input())
l = []
for i in range(n):
    s,t = input().split()
    l.append([s,int(t)])
already = set()
maximum = 0
answer = 0
for i in range(n):
    if l[i][0] not in already:
        already.add(l[i][0])
        if maximum < l[i][1]:
            answer = i
            maximum = l[i][1]
print(answer+1)