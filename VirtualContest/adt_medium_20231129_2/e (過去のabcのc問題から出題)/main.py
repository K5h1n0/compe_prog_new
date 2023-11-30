n,k = map(int,input().split())
a = set(list(map(int,input().split())))
for i in range(k):
    if i in a:
        continue
    print(i)
    exit()
print(k)